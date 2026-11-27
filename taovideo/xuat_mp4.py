"""Lớp xuất dự phòng: ghi kế hoạch dựng thành MP4 bản nháp + file phụ đề .srt bằng FFmpeg."""

from __future__ import annotations

import os
import subprocess
import tempfile
import textwrap
from typing import List

from .ke_hoach import KeHoach


def _srt_time(s: float) -> str:
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3_600_000)
    m, ms = divmod(ms, 60_000)
    sec, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{sec:02},{ms:03}"


def ghi_srt(kh: KeHoach, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        for i, ch in enumerate(kh.chu, 1):
            f.write(f"{i}\n{_srt_time(ch.bat_dau)} --> {_srt_time(ch.bat_dau + ch.do_dai)}\n{ch.noi_dung}\n\n")


def _escape_path(p: str) -> str:
    # Đường dẫn Windows trong filter FFmpeg: dùng / và escape dấu :
    return p.replace("\\", "/").replace(":", "\\:")


def xuat_mp4(kh: KeHoach, path_mp4: str, font: str) -> str:
    """Xuất MP4 9:16 bản nháp. Trả về đường dẫn MP4 (kèm .srt cùng tên)."""
    os.makedirs(os.path.dirname(os.path.abspath(path_mp4)), exist_ok=True)
    W, H, FPS = kh.rong, kh.cao, kh.fps
    args: List[str] = ["ffmpeg", "-y", "-v", "error"]
    f: List[str] = []

    for i, c in enumerate(kh.clips):
        args += ["-ss", f"{c.tu:.3f}", "-t", f"{c.do_dai:.3f}", "-i", c.file]
        f.append(f"[{i}:v]scale={W}:{H}:force_original_aspect_ratio=decrease,pad={W}:{H}:(ow-iw)/2:(oh-ih)/2,"
                 f"setsar=1,fps={FPS},format=yuv420p[v{i}]")
        f.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}]")
    n = len(kh.clips)
    f.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[nen][am]")

    cur = "nen"
    for j, lp in enumerate(kh.lop_phu):
        idx = n + j
        if lp.kieu == "trong_suot" and lp.file.lower().endswith(".webm"):
            args += ["-c:v", "libvpx-vp9"]   # bộ giải mã giữ kênh trong suốt của VP9
        args += ["-itsoffset", f"{lp.bat_dau:.3f}", "-i", lp.file]
        src = f"[{idx}:v]scale={W}:{H},setpts=PTS"
        if lp.kieu == "phong_xanh":
            src += ",colorkey=0x00FF00:0.3:0.1"
        f.append(src + f"[lp{j}]")
        f.append(f"[{cur}][lp{j}]overlay=0:0:eof_action=pass:"
                 f"enable='between(t,{lp.bat_dau:.3f},{lp.bat_dau + lp.do_dai:.3f})'[o{j}]")
        cur = f"o{j}"

    tmpdir = tempfile.mkdtemp(prefix="xuat_mp4_")
    for k, ch in enumerate(kh.chu):
        # Xuống dòng khoảng 26 ký tự để chữ không tràn khung 9:16
        tf = os.path.join(tmpdir, f"chu{k}.txt")
        with open(tf, "w", encoding="utf-8") as fh:
            fh.write("\n".join(textwrap.wrap(ch.noi_dung, 26)))
        f.append(f"[{cur}]drawtext=fontfile='{_escape_path(font)}':textfile='{_escape_path(tf)}':"
                 f"text_align=center:fontsize=64:fontcolor=white:borderw=5:bordercolor=black:x=(w-tw)/2:y=h*0.72:"
                 f"enable='between(t,{ch.bat_dau:.3f},{ch.bat_dau + ch.do_dai:.3f})'[t{k}]")
        cur = f"t{k}"

    args += ["-filter_complex", ";".join(f), "-map", f"[{cur}]", "-map", "[am]",
             "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "160k",
             "-movflags", "+faststart", "-t", f"{kh.tong_do_dai:.3f}", path_mp4]
    subprocess.run(args, check=True)
    ghi_srt(kh, os.path.splitext(path_mp4)[0] + ".srt")
    return path_mp4
