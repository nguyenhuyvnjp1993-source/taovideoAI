# Kết quả chặng C1

Ngày chạy: 28/11/2026 (giờ Nhật), trên máy Windows của Huy (DESKTOP-6M44C7D).

## Kết luận

**CapCut dùng được. Đi tiếp với lớp xuất CapCut, không cần chuyển sang MP4.**

- CapCut **9.9.0.4252** tự thấy dự án do code tạo, **không cần** sửa `root_meta_info.json`.
- Clip, thứ tự, độ dài, chữ tiếng Việt có dấu và lớp phủ đều hiện đúng. Sửa, lưu, thoát, mở lại không bị hỏng.
- Lớp phủ đồ họa: dùng **MOV ProRes 4444 có kênh trong suốt**. WebM trong suốt **không** được (nền đen). Nền xanh lá + xóa phông xanh cũng chạy tốt, dùng làm dự phòng.
- Bản MP4 dự phòng bằng FFmpeg chạy được từ cùng kế hoạch dựng.

## Máy và phiên bản

| Thành phần | Bản |
| --- | --- |
| CapCut | 9.9.0.4252 (bản 9.8.0.4213 vẫn còn trong máy, dùng để lùi về) |
| pyCapCut | 0.0.4 |
| Python | 3.13.17 |
| FFmpeg | 9.1 (gyan.dev) |
| Định dạng dự án CapCut thật trên máy | version 360000, new_version 193.0.0 |
| Định dạng pyCapCut ghi ra | new_version 140.0.0 (CapCut 9.9 vẫn mở được) |

## Từng bài thử

| # | Bài thử | Kết quả | Ghi chú |
| --- | --- | --- | --- |
| T1 | Môi trường Windows | Đạt | Python, FFmpeg, Git có sẵn; ghi được vào thư mục dự án CapCut |
| T2 | Cowork chạm được tới đâu | Chưa thử | C1 chạy bằng phiên điều khiển máy (Python trên Windows), không qua Cowork. Kiểm lại ở C6 khi đóng gói Skill |
| T3 | Đọc dự án thật | Đạt | JSON thường, không mã hóa. `root_meta_info.json` có khóa `all_draft_store`, `draft_ids`, `root_path` |
| T4 | Dự án tối thiểu | **Đạt** | 3 clip × 4 giây, đúng thứ tự, tổng 12 giây |
| T5 | Đăng ký dự án | Không cần | CapCut 9.9 tự quét thư mục và thấy cả 5 dự án |
| T6 | Đường dẫn Windows | **Đạt** | Script chạy bằng Python trên Windows; không báo thiếu file |
| T7 | Chữ tiếng Việt | Đạt (cần chỉnh) | Dấu hiện đúng. Chữ nằm quá cao và ngắt giữa từ; đã sửa vị trí xuống phía dưới trong code. Font Be Vietnam Pro chưa có trong danh sách font của pyCapCut, đang dùng font hệ thống: để lại cho C5 |
| T8 | Lớp phủ trong suốt | **MOV đạt, WebM không** | WebM VP9 alpha hiện nền đen; MOV ProRes 4444 thấy rõ video bên dưới |
| T9 | Phông xanh | **Đạt** | File dự án tự bật xóa phông xanh, viền thẻ sạch |
| T10 | MP4 dự phòng | Đạt | MP4 1080×1920, 12 giây, kèm `.srt`. Chưa thử phát trên điện thoại |
| T11 | Độ bền | **Đạt** | Mở dự án, xóa lớp chữ, CapCut tự lưu, thoát hẳn, mở lại: thay đổi còn nguyên, không báo hỏng |
| T12 | Thời gian | Đạt với clip thử | Script chạy hết 3,6 giây (5 dự án + MP4). Chưa đo với 3 video thật của chị: cần làm ở C3 khi có Whisper |

## Lưu ý cho các chặng sau

1. **Khóa bản CapCut:** máy đang bật kênh beta (`joinBeta=true`) và tự tải 9.9 về mà không hỏi. Nên tắt beta và chặn cập nhật, vì brief ghi bản 10.x báo file do code tạo là hỏng.
2. **Lớp phủ dùng MOV ProRes 4444.** File khá nặng (khoảng 7 MB mỗi giây ở 1080×1920). Nếu dung lượng thành vấn đề thì chuyển sang nền xanh lá.
3. **Phải thoát hẳn CapCut trước khi script ghi dự án.** Lúc CapCut chạy, nó tự ghi lại `root_meta_info.json`.
4. Dự án mới hiện `00:00` trong danh sách cho tới lần mở đầu tiên; mở ra là CapCut tự cập nhật.
5. Các dự án thử `C1-…` vẫn để trong CapCut của Huy, xóa được bất cứ lúc nào.

## Cách Huy tự kiểm lại

1. Thoát hẳn CapCut (cả biểu tượng ở khay hệ thống).
2. Mở PowerShell, chạy:
   ```
   cd C:\VideoBDS\taovideoAI
   .venv\Scripts\python c1\chay_c1.py
   ```
3. Mở CapCut, thấy 5 dự án `C1-1` đến `C1-5`. Mở `C1-4-trong-suot-mov`, kéo đầu phát tới giây thứ 5: thẻ giá hiện trên nền clip màu đỏ.
4. Bản MP4 dự phòng nằm ở `C:\VideoBDS\output\C1-ban-nhap.mp4`.
