"""Chạy các bài thử C1 trên máy Windows có CapCut.

Cách chạy (trong thư mục repo):
    python c1/chay_c1.py              # tạo các dự án thử + MP4 dự phòng
    python c1/chay_c1.py --kiem-tra   # chỉ kiểm tra máy (T1, T3), không ghi gì vào CapCut
    python c1/chay_c1.py --dang-ky    # như trên, thêm bước đăng ký dự án vào root_meta_info.json (T5)

Trước khi chạy: thoát hẳn CapCut (kể cả biểu tượng ở khay hệ thống).
Kết quả và thời gian từng bước ghi vào <thu_muc_ra>/c1_ketqua.json.
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import time

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, REPO)

from taovideo.ke_hoach import doc_ke_hoach, chi_giu  # noqa: E402

DUOI_VIDEO = (".mp4", ".mov", ".m4v", ".MP4", ".MOV")


class DongHo:
    """Ghi thời gian từng bước (cho bài thử T12)."""

    def __init__(self):
        self.bat_dau = time.time()
        self.buoc = []

    def __call__(self, ten):
        dh = self

        class _B:
            def __enter__(self):
                self.t = time.time()
                print(f"\n== {ten}")

            def __exit__(self, *exc):
                giay = time.time() - self.t
                dh.buoc.append({"buoc": ten, "giay": round(giay, 2), "loi": repr(exc[1]) if exc[1] else None})
                print(f"   ({giay:.1f}s{' - LỖI' if exc[1] else ''})")
                return False
        return _B()

    def tong(self):
        return round(time.time() - self.bat_dau, 2)


def doc_config():
    p = os.path.join(REPO, "config.json")
    if not os.path.exists(p):
        sys.exit("Chưa có config.json. Chép config.example.json thành config.json rồi sửa đường dẫn.")
    with open(p, encoding="utf-8") as f:
        cfg = json.load(f)
    cfg["thu_muc_du_an_capcut"] = os.path.expandvars(cfg["thu_muc_du_an_capcut"])
    return cfg


def capcut_dang_chay() -> bool:
    if platform.system() != "Windows":
        return False
    out = subprocess.run(["tasklist", "/FI", "IMAGENAME eq CapCut.exe"], capture_output=True, text=True).stdout
    return "CapCut.exe" in out


def tim_video(thu_muc):
    return sorted(p for p in glob.glob(os.path.join(thu_muc, "*")) if p.endswith(DUOI_VIDEO))


def tao_clip_gia(thu_muc, so_luong=3):
    """Không có đủ clip thật thì tạo clip thử 9:16 có tiếng (8 giây) bằng FFmpeg."""
    os.makedirs(thu_muc, exist_ok=True)
    mau = ["0x1F3A93", "0x8E2C2C", "0x5A3E8C"]
    for i in range(1, so_luong + 1):
        p = os.path.join(thu_muc, f"clip{i}.mp4")
        if os.path.exists(p) and os.path.getsize(p) > 0:
            continue
        tam = p + ".tmp"   # ghi ra file tạm, xong mới đổi tên, để lỗi không để lại file rỗng
        # Thanh trắng chạy ngang phía trên để dễ thấy đoạn cắt (overlay, chạy được trên FFmpeg 9.x)
        subprocess.run([
            "ffmpeg", "-y", "-v", "error",
            "-f", "lavfi", "-i", f"color=c={mau[i - 1]}:s=1080x1920:r=30:d=8",
            "-f", "lavfi", "-i", "color=c=white:s=1080x60:r=30:d=8",
            "-f", "lavfi", "-i", f"sine=frequency={300 + 100 * i}:duration=8",
            "-filter_complex", "[0][1]overlay=x='-w+w*t/8':y=0[v]", "-map", "[v]", "-map", "2",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", "-f", "mp4", tam], check=True)
        os.replace(tam, p)
        print(f"   Tạo clip thử: {p}")


def kiem_tra_may(cfg, ket_qua):
    """T1 + T3: phiên bản công cụ, thư mục dự án CapCut, cấu trúc root_meta_info.json."""
    def ban(cmd):
        try:
            return subprocess.run(cmd, capture_output=True, text=True).stdout.splitlines()[0]
        except Exception as e:  # noqa: BLE001
            return f"không chạy được: {e}"

    kq = {
        "python": sys.version.split()[0],
        "ffmpeg": ban(["ffmpeg", "-version"]),
        "pycapcut": __import__("importlib.metadata").metadata.version("pycapcut"),
    }
    local = os.environ.get("LOCALAPPDATA", "")
    kq["ban_capcut_trong_Apps"] = sorted(os.path.basename(p) for p in glob.glob(os.path.join(local, "CapCut", "Apps", "*.*.*.*")))
    td = cfg["thu_muc_du_an_capcut"]
    kq["thu_muc_du_an_ton_tai"] = os.path.isdir(td)
    if kq["thu_muc_du_an_ton_tai"]:
        kq["du_an"] = sorted(d for d in os.listdir(td)
                             if os.path.isdir(os.path.join(td, d)) and not d.startswith("."))
        # Ghi thử 1 file rồi xóa
        p = os.path.join(td, "_c1_ghi_thu.txt")
        try:
            with open(p, "w") as f:
                f.write("ok")
            os.remove(p)
            kq["ghi_duoc"] = True
        except OSError as e:
            kq["ghi_duoc"] = f"không: {e}"
        root = os.path.join(td, "root_meta_info.json")
        if os.path.exists(root):
            with open(root, encoding="utf-8") as f:
                r = json.load(f)
            kq["root_meta_khoa"] = list(r.keys())
            ds = r.get("all_draft_store") or []
            kq["root_meta_so_du_an"] = len(ds)
            kq["root_meta_khoa_moi_du_an"] = list(ds[0].keys()) if ds else []
        for ten in kq.get("du_an", [])[:1]:
            p = os.path.join(td, ten, "draft_content.json")
            if os.path.exists(p):
                with open(p, encoding="utf-8") as f:
                    dc = json.load(f)
                kq["mau_draft_version"] = {"version": dc.get("version"), "new_version": dc.get("new_version"),
                                           "platform": dc.get("platform", {}).get("app_version")}
    ket_qua["kiem_tra_may"] = kq
    print(json.dumps(kq, ensure_ascii=False, indent=2))


_DA_SAO_LUU = set()


def sao_luu_root_meta(td):
    """Sao lưu root_meta_info.json một lần mỗi lần chạy (giữ bản gốc trước mọi thay đổi)."""
    root = os.path.join(td, "root_meta_info.json")
    if root in _DA_SAO_LUU:
        return root
    _DA_SAO_LUU.add(root)
    bk = root + time.strftime(".c1-backup-%Y%m%d-%H%M%S")
    shutil.copy2(root, bk)
    print(f"   Đã sao lưu: {bk}")
    return root


def dang_ky_du_an(td, ten_du_an):
    """T5: thêm dự án vào root_meta_info.json bằng cách chép mục của một dự án có sẵn rồi đổi tên/đường dẫn.

    Luôn sao lưu root_meta_info.json trước. Chỉ dùng khi CapCut không tự thấy dự án mới.
    """
    import uuid
    root = sao_luu_root_meta(td)
    with open(root, encoding="utf-8") as f:
        r = json.load(f)
    ds = r.get("all_draft_store") or []
    if not ds:
        raise RuntimeError("root_meta_info.json không có dự án mẫu nào để chép")
    thu_muc_moi = os.path.join(td, ten_du_an)
    ds = [x for x in ds if os.path.normcase(os.path.normpath(x.get("draft_fold_path", ""))) != os.path.normcase(os.path.normpath(thu_muc_moi))]
    mau = ds[0]
    cu = os.path.normpath(mau.get("draft_fold_path", ""))
    moi = dict(mau)
    for k, v in mau.items():
        if isinstance(v, str) and cu and v.replace("/", "\\").startswith(cu.replace("/", "\\")):
            moi[k] = thu_muc_moi + v.replace("/", "\\")[len(cu.replace("/", "\\")):]
    now_us = int(time.time() * 1_000_000)
    moi.update({"draft_name": ten_du_an, "draft_fold_path": thu_muc_moi,
                "draft_id": str(uuid.uuid4()).upper()})
    for k in ("tm_draft_create", "tm_draft_modified"):
        if k in moi:
            moi[k] = now_us
    ds.insert(0, moi)
    r["all_draft_store"] = ds
    with open(root, "w", encoding="utf-8") as f:
        json.dump(r, f, ensure_ascii=False)
    print(f"   Đã đăng ký {ten_du_an} vào root_meta_info.json")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kiem-tra", action="store_true", help="chỉ kiểm tra máy, không tạo dự án")
    ap.add_argument("--dang-ky", action="store_true", help="đăng ký dự án vào root_meta_info.json (T5)")
    ap.add_argument("--bo-qua-capcut-dang-chay", action="store_true")
    a = ap.parse_args()

    cfg = doc_config()
    os.makedirs(cfg["thu_muc_ra"], exist_ok=True)
    dh = DongHo()
    ket_qua = {"thoi_diem": time.strftime("%Y-%m-%d %H:%M:%S")}

    with dh("Kiểm tra máy (T1, T3)"):
        kiem_tra_may(cfg, ket_qua)
    if a.kiem_tra:
        _ghi(cfg, ket_qua, dh)
        return

    if capcut_dang_chay() and not a.bo_qua_capcut_dang_chay:
        sys.exit("CapCut đang chạy. Thoát hẳn CapCut (cả biểu tượng ở khay hệ thống) rồi chạy lại.")

    with dh("Chuẩn bị 3 clip"):
        if len(tim_video(cfg["thu_muc_video"])) < 3:
            tao_clip_gia(cfg["thu_muc_video"])
        videos = tim_video(cfg["thu_muc_video"])[:3]
        print("   Dùng:", *[os.path.basename(v) for v in videos])

    with dh("Chuyển lớp phủ WebM sang MOV ProRes 4444"):
        webm = os.path.join(REPO, "c1", "assets", "the_gia_alpha.webm")
        mov = os.path.join(REPO, "c1", "assets", "the_gia_alpha.mov")
        if not os.path.exists(mov):
            subprocess.run(["ffmpeg", "-y", "-v", "error", "-c:v", "libvpx-vp9", "-i", webm,
                            "-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", mov], check=True)

    with dh("Đọc kế hoạch dựng"):
        with open(os.path.join(REPO, "c1", "ke_hoach_mau.json"), encoding="utf-8") as f:
            d = json.load(f)
        for c, v in zip(d["clips"], videos):
            c["file"] = v
        tmp = os.path.join(tempfile.gettempdir(), "c1_ke_hoach.json")
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False)
        kh = doc_ke_hoach(tmp, cfg["thu_muc_video"], REPO)
        print(f"   {len(kh.clips)} clip, tổng {kh.tong_do_dai:.1f}s")

    from taovideo.xuat_capcut import xuat_capcut
    bien_the = [
        ("C1-1-toi-thieu", chi_giu(kh, chu=False, ten="C1-1-toi-thieu")),                       # T4, T6
        ("C1-2-chu", chi_giu(kh, chu=True, ten="C1-2-chu")),                                      # T7
        ("C1-3-trong-suot-webm", chi_giu(kh, chu=False, kieu_lop_phu="trong_suot", ten="C1-3-trong-suot-webm")),  # T8
        ("C1-4-trong-suot-mov", chi_giu(kh, chu=False, kieu_lop_phu="trong_suot", doi_file_lop_phu=mov,
                                        ten="C1-4-trong-suot-mov")),                             # T8
        ("C1-5-phong-xanh", chi_giu(kh, chu=False, kieu_lop_phu="phong_xanh", ten="C1-5-phong-xanh")),  # T9
    ]
    ket_qua["du_an"] = []
    for ten, k in bien_the:
        with dh(f"Tạo dự án CapCut {ten}"):
            p = xuat_capcut(k, cfg["thu_muc_du_an_capcut"])
            ket_qua["du_an"].append({"ten": ten, "file": p})
            if a.dang_ky:
                dang_ky_du_an(cfg["thu_muc_du_an_capcut"], ten)

    from taovideo.xuat_mp4 import xuat_mp4
    with dh("Xuất MP4 dự phòng (T10)"):
        k = chi_giu(kh, chu=True, kieu_lop_phu="trong_suot", ten="C1-ban-nhap")
        out = xuat_mp4(k, os.path.join(cfg["thu_muc_ra"], "C1-ban-nhap.mp4"), cfg["font_ffmpeg"])
        ket_qua["mp4"] = out
        print("  ", out)

    _ghi(cfg, ket_qua, dh)
    print("\nXong. Mở CapCut, tìm các dự án bắt đầu bằng 'C1-'.")


def _ghi(cfg, ket_qua, dh):
    ket_qua["buoc"] = dh.buoc
    ket_qua["tong_giay"] = dh.tong()
    p = os.path.join(cfg["thu_muc_ra"], "c1_ketqua.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(ket_qua, f, ensure_ascii=False, indent=2)
    print(f"\nTổng thời gian: {ket_qua['tong_giay']}s. Kết quả: {p}")


if __name__ == "__main__":
    main()
