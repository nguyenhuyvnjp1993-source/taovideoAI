"""Lớp lõi: kế hoạch dựng.

Kế hoạch dựng là một file JSON, không phụ thuộc CapCut, mô tả:
- clip nào, cắt từ giây nào đến giây nào (nối liền nhau trên dòng thời gian chính);
- chữ gì, hiện lúc nào, bao lâu;
- lớp phủ đồ họa nào, hiện lúc nào, kiểu nền (trong suốt hay phông xanh).

Lớp xuất (xuat_capcut.py, xuat_mp4.py) chỉ đọc kế hoạch này.
"""

from __future__ import annotations

import json
import os
import subprocess
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Clip:
    file: str          # đường dẫn tuyệt đối trên máy chạy code
    tu: float          # giây bắt đầu cắt trong file gốc
    den: float         # giây kết thúc cắt trong file gốc

    @property
    def do_dai(self) -> float:
        return self.den - self.tu


@dataclass
class Chu:
    noi_dung: str
    bat_dau: float
    do_dai: float


@dataclass
class LopPhu:
    file: str
    bat_dau: float
    do_dai: float
    kieu: str = "trong_suot"   # "trong_suot" hoặc "phong_xanh"


@dataclass
class KeHoach:
    ten: str
    rong: int = 1080
    cao: int = 1920
    fps: int = 30
    clips: List[Clip] = field(default_factory=list)
    chu: List[Chu] = field(default_factory=list)
    lop_phu: List[LopPhu] = field(default_factory=list)

    @property
    def tong_do_dai(self) -> float:
        return sum(c.do_dai for c in self.clips)


def do_dai_video(path: str) -> float:
    """Đọc độ dài video bằng ffprobe (giây)."""
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "default=nokey=1:noprint_wrappers=1", path],
        capture_output=True, text=True, check=True).stdout.strip()
    return float(out)


def _tuyet_doi(path: str, goc: str) -> str:
    return os.path.abspath(path if os.path.isabs(path) else os.path.join(goc, path))


def doc_ke_hoach(path: str, thu_muc_video: str, thu_muc_repo: str) -> KeHoach:
    """Đọc kế hoạch JSON, đổi đường dẫn thành tuyệt đối và kiểm tra.

    - Đường dẫn clip tương đối tính theo thu_muc_video.
    - Đường dẫn lớp phủ tương đối tính theo thu_muc_repo.
    - Đoạn cắt vượt quá độ dài file gốc thì cắt bớt cho vừa (ghi cảnh báo).
    """
    with open(path, encoding="utf-8") as f:
        d = json.load(f)

    kh = KeHoach(ten=d["ten"], rong=d.get("rong", 1080), cao=d.get("cao", 1920), fps=d.get("fps", 30))
    loi: List[str] = []

    for c in d.get("clips", []):
        p = _tuyet_doi(c["file"], thu_muc_video)
        if not os.path.exists(p):
            loi.append(f"Không thấy clip: {p}")
            continue
        dai = do_dai_video(p)
        tu, den = float(c.get("tu", 0)), float(c.get("den", dai))
        if den > dai:
            print(f"  [cảnh báo] {os.path.basename(p)} chỉ dài {dai:.2f}s, cắt bớt đoạn đến {dai:.2f}s")
            den = dai
        if not 0 <= tu < den:
            loi.append(f"Đoạn cắt sai ở {p}: từ {tu} đến {den}")
            continue
        kh.clips.append(Clip(p, tu, den))

    for t in d.get("chu", []):
        kh.chu.append(Chu(t["noi_dung"], float(t["bat_dau"]), float(t["do_dai"])))

    for lp in d.get("lop_phu", []):
        p = _tuyet_doi(lp["file"], thu_muc_repo)
        if not os.path.exists(p):
            loi.append(f"Không thấy lớp phủ: {p}")
            continue
        kh.lop_phu.append(LopPhu(p, float(lp["bat_dau"]), float(lp["do_dai"]), lp.get("kieu", "trong_suot")))

    if not kh.clips:
        loi.append("Kế hoạch không có clip nào dùng được")
    for x in kh.chu + kh.lop_phu:
        if x.bat_dau + x.do_dai > kh.tong_do_dai + 1e-6:
            loi.append(f"Phần tử hiện quá cuối video ({x.bat_dau}+{x.do_dai} > {kh.tong_do_dai:.2f}s)")
    if loi:
        raise ValueError("Kế hoạch dựng có lỗi:\n  " + "\n  ".join(loi))
    return kh


def chi_giu(kh: KeHoach, *, chu: bool = True, kieu_lop_phu: Optional[str] = None,
            doi_file_lop_phu: Optional[str] = None, ten: Optional[str] = None) -> KeHoach:
    """Tạo bản sao kế hoạch chỉ giữ một số phần (dùng để tách bài thử C1)."""
    lp = [l for l in kh.lop_phu if kieu_lop_phu and l.kieu == kieu_lop_phu]
    if doi_file_lop_phu:
        lp = [LopPhu(doi_file_lop_phu, l.bat_dau, l.do_dai, l.kieu) for l in lp]
    return KeHoach(ten=ten or kh.ten, rong=kh.rong, cao=kh.cao, fps=kh.fps,
                   clips=list(kh.clips), chu=list(kh.chu) if chu else [], lop_phu=lp)
