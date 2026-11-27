# taovideoAI

Tự động dựng khung video BĐS (Claude + CapCut bản máy tính trên Windows).

- Tài liệu dự án: [docs/brief.md](docs/brief.md)
- Thiết kế đồ họa chuyển động: [docs/motion.md](docs/motion.md)
- Hướng dẫn cho Claude: [CLAUDE.md](CLAUDE.md)

## Cấu trúc

| Thư mục | Vai trò |
| --- | --- |
| `taovideo/ke_hoach.py` | Lớp lõi: kế hoạch dựng (clip, chữ, lớp phủ), không phụ thuộc CapCut |
| `taovideo/xuat_capcut.py` | Lớp xuất: ghi kế hoạch thành dự án CapCut (pyCapCut 0.0.4) |
| `taovideo/xuat_mp4.py` | Lớp xuất dự phòng: ghi kế hoạch thành MP4 + phụ đề bằng FFmpeg |
| `c1/` | Bài thử chặng C1 |

## Cài trên máy Windows

```
git clone https://github.com/nguyenhuyvnjp1993-source/taovideoAI C:\VideoBDS\taovideoAI
cd C:\VideoBDS\taovideoAI
py -3.13 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
copy config.example.json config.json   (rồi sửa đường dẫn trong config.json)
```

## Trạng thái các chặng

| Chặng | Trạng thái |
| --- | --- |
| C1: Kiểm chứng CapCut + pyCapCut | **Xong**, CapCut 9.9 dùng được. Xem [docs/c1-ketqua.md](docs/c1-ketqua.md) |
| C2–C7 | Chưa bắt đầu |
