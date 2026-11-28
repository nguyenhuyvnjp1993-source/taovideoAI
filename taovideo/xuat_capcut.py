"""Lớp xuất CapCut: ghi kế hoạch dựng thành dự án CapCut bản máy tính bằng pyCapCut 0.0.4.

Lưu ý (đã kiểm trong mã pyCapCut 0.0.4):
- pyCapCut ghi đường dẫn tuyệt đối của video theo máy đang chạy code, nên phải chạy
  bằng Python trên chính máy Windows có CapCut.
- pyCapCut KHÔNG đăng ký dự án vào root_meta_info.json.
"""

from __future__ import annotations

import pycapcut as cc
from pycapcut import trange_seconds

from .ke_hoach import KeHoach

MAU_XANH_LA = "#00FF00FF"


def xuat_capcut(kh: KeHoach, thu_muc_du_an: str, *, ghi_de: bool = True) -> str:
    """Tạo dự án CapCut tên kh.ten trong thu_muc_du_an. Trả về đường dẫn draft_content.json."""
    thu_muc = cc.DraftFolder(thu_muc_du_an)
    script = thu_muc.create_draft(kh.ten, kh.rong, kh.cao, kh.fps, allow_replace=ghi_de)

    # Dòng thời gian chính: các clip nối liền nhau từ 0s
    script.add_track(cc.TrackType.video)
    t = 0.0
    for c in kh.clips:
        seg = cc.VideoSegment(
            c.file,
            trange_seconds(t, duration=c.do_dai),
            source_timerange=trange_seconds(c.tu, duration=c.do_dai),
        )
        script.add_segment(seg)
        t += c.do_dai

    # Lớp phủ đồ họa (mỗi lớp phủ một track riêng, nằm trên video chính)
    for i, lp in enumerate(kh.lop_phu):
        ten_track = f"lop_phu_{i + 1}"
        script.add_track(cc.TrackType.video, ten_track, relative_index=i + 1)
        seg = cc.VideoSegment(lp.file, trange_seconds(lp.bat_dau, duration=lp.do_dai))
        if lp.kieu == "phong_xanh":
            seg.add_chroma(MAU_XANH_LA, intensity=20)
        script.add_segment(seg, ten_track)

    # Chữ
    if kh.chu:
        script.add_track(cc.TrackType.text)
        for ch in kh.chu:
            script.add_segment(cc.TextSegment(
                ch.noi_dung,
                trange_seconds(ch.bat_dau, duration=ch.do_dai),
                style=cc.TextStyle(size=9.0, bold=True, color=(1.0, 1.0, 1.0), align=1,
                                   auto_wrapping=True, max_line_width=0.8),
                border=cc.TextBorder(color=(0.0, 0.0, 0.0), width=40.0),
                clip_settings=cc.ClipSettings(transform_y=-0.45),  # âm = phía dưới; tránh 450px đáy (Reels/TikTok)
            ))

    script.save()
    return script.save_path
