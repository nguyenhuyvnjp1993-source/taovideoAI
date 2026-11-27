# Kế hoạch chặng C1: kiểm chứng CapCut 9.5 + pyCapCut 0.0.4 trên Windows

Trạng thái: **chờ Huy duyệt**. Chưa viết code C1.

## 1. Mục tiêu của C1

Trả lời một câu hỏi duy nhất trước khi tốn công cho các chặng sau:

> Trên máy Windows của Huy, code có tạo được một file dự án CapCut mà CapCut 9.5 mở ra đúng (clip, chữ, lớp phủ đồ họa) hay không?

- **Có** → các chặng sau tiếp tục với lớp xuất CapCut.
- **Không** → theo brief, dự án chuyển hẳn sang xuất MP4 bằng FFmpeg (điểm quyết định sau C1).

C1 chỉ là thử nghiệm kỹ thuật. Chưa có kịch bản, chưa có Whisper cắt câu vấp, chưa có 5 mẫu đồ họa thật.

## 2. Những gì đã kiểm trước trong mã nguồn pyCapCut 0.0.4

Claude đã tải gói `pycapcut==0.0.4` và đọc mã. Ba điều ảnh hưởng trực tiếp tới kế hoạch:

1. **pyCapCut không đăng ký dự án với CapCut.** Hàm tạo dự án chỉ tạo thư mục, chép `draft_meta_info.json` mẫu và ghi `draft_content.json`. Nó **không** sửa `root_meta_info.json`. Vì vậy C1 phải tự kiểm xem CapCut 9.5 có tự thấy dự án mới không, và nếu không thì phải bổ sung bước đăng ký.
2. **Đường dẫn video bị “đóng băng” lúc chạy code.** Thư viện đổi đường dẫn thành đường dẫn tuyệt đối và kiểm tra file có tồn tại ngay trên máy đang chạy code. Nếu code chạy trong môi trường Linux của Cowork thì JSON sẽ chứa đường dẫn kiểu `/mnt/...`, CapCut trên Windows không đọc được. Kết luận: **script tạo dự án phải chạy bằng Python cài trên Windows** (hoặc phải có bước đổi đường dẫn sang `C:\...`). C1 kiểm cả hai cách và chọn một.
3. **Xóa phông xanh (chroma) được tác giả ghi là đã thử trên CapCut 9.5.0.4050.** Đây là phương án dự phòng cho nền trong suốt, nên khả năng cao dùng được. Nền trong suốt thật thì thư viện không ghi gì, phải tự thử.

Thêm: tác giả báo bản 0.1.0 sẽ đổi giao diện (bỏ `add_track`), nên khóa đúng `pycapcut==0.0.4` là cần thiết.

## 3. Việc Huy chuẩn bị trước khi chạy C1

| # | Việc | Ghi chú |
| --- | --- | --- |
| P1 | Xem CapCut trên máy đang là bản nào (Cài đặt → Giới thiệu). Nếu là 10.x thì gỡ và cài 9.5 | Ghi lại số bản đầy đủ, ví dụ 9.5.0.4050 |
| P2 | Chặn CapCut tự cập nhật | Claude sẽ viết hướng dẫn từng bước khi chạy C1 |
| P3 | 3 clip ngắn quay dọc bất kỳ (5–20 giây) | Để trong một thư mục cố định, ví dụ `C:\VideoBDS\test-c1\` |
| P4 | Tạo bằng tay 1 dự án CapCut trống tên `MAU-C1`, thêm 1 clip, thoát CapCut | Dùng làm dự án gốc “thật” để so sánh và làm mẫu |
| P5 | Cài Python 3.11 cho Windows (nếu chưa có) và FFmpeg | Claude sẽ hướng dẫn hoặc tự cài qua phiên điều khiển máy nếu Huy cho phép |

## 4. Các bài thử

Mỗi bài thử có kết quả **Đạt / Không đạt** và được ghi vào `docs/c1-ketqua.md`.

| # | Bài thử | Cách thử | Đạt khi |
| --- | --- | --- | --- |
| T1 | Môi trường Windows | Chạy Python, FFmpeg trên máy Huy; tìm thư mục dự án CapCut (thường trong `AppData\Local\CapCut\User Data\Projects\com.lveditor.draft`) và ghi thử 1 file vào đó | Cả ba chạy được, ghi được file |
| T2 | Cowork chạm được tới đâu | Từ Claude Desktop (Cowork) thử đọc/ghi thư mục dự án CapCut và gọi Python, FFmpeg | Ghi rõ được gì / không được gì. Không đạt cũng không sao, chỉ quyết định script chạy ở đâu |
| T3 | Đọc dự án thật | Script đọc dự án `MAU-C1` Huy tạo tay, liệt kê cấu trúc thư mục và `root_meta_info.json` | Hiểu được CapCut 9.5 ghi những gì, dự án có bị mã hóa không |
| T4 | Dự án tối thiểu | Script tạo dự án mới 1080×1920, 3 clip nối nhau, cắt mỗi clip một đoạn | Thoát hẳn CapCut, mở lại: dự án hiện trong danh sách, 3 clip đúng thứ tự, đúng độ dài |
| T5 | Đăng ký dự án | Nếu T4 dự án không hiện: thêm bước ghi vào `root_meta_info.json` (sao lưu file trước) | Dự án hiện sau khi mở lại CapCut |
| T6 | Đường dẫn Windows | So sánh chạy script bằng Python Windows và chạy trong Cowork + đổi đường dẫn | Clip không báo “thiếu file” trong CapCut |
| T7 | Chữ tiêu đề tiếng Việt | Thêm 1 dòng chữ có dấu (ví dụ “Đất nền 120m² – xã X, tỉnh Hưng Yên”) với font Be Vietnam Pro | Hiện đúng dấu, đúng font, sửa được trong CapCut |
| T8 | Lớp phủ nền trong suốt | Dựng 1 clip đồ họa thử 3 giây (thẻ giá, chữ giả) bằng HTML → video có kênh trong suốt (WebM VP9 alpha và MOV ProRes 4444), đặt lên lớp phủ | Thấy video bên dưới, không bị nền đen |
| T9 | Dự phòng phông xanh | Cùng clip đồ họa trên nền xanh lá, file dự án tự bật xóa phông xanh | Nền xanh biến mất, kéo/xóa lớp phủ được |
| T10 | Dự phòng MP4 | Từ cùng kế hoạch dựng của T4, FFmpeg xuất 1 MP4 bản nháp kèm file phụ đề `.srt` thử | MP4 phát được trên điện thoại, đúng 9:16 |
| T11 | Độ bền | Mở dự án, sửa một chút, lưu, thoát, mở lại | Không báo hỏng, không mất clip |

Lưu ý: T4–T9 phải **thoát hẳn CapCut** (kể cả biểu tượng ở khay hệ thống) trước khi script ghi file, rồi mới mở lại.

## 5. Claude sẽ làm gì khi C1 được duyệt

Chỉ làm đủ để chạy các bài thử trên, không thêm tính năng:

- `requirements.txt` khóa `pycapcut==0.0.4`.
- Một file **kế hoạch dựng mẫu** (JSON) mô tả 3 clip + 1 chữ + 1 lớp phủ: đây là bản nháp đầu tiên của “lớp lõi”, chưa phụ thuộc CapCut.
- Script **xuất CapCut** đọc kế hoạch đó và ghi dự án (T4–T9).
- Script **xuất MP4** bằng FFmpeg đọc cùng kế hoạch đó (T10).
- Script dựng clip đồ họa thử từ HTML bằng trình duyệt ẩn (T8–T9).
- Script kiểm tra môi trường (T1) và sao lưu `root_meta_info.json` trước khi động vào.
- File cấu hình mẫu `config.example.json` (đường dẫn thư mục, tên, số Zalo để trống). File cấu hình thật **không commit**.
- `docs/c1-ketqua.md` ghi kết quả từng bài thử và kết luận: đi tiếp CapCut hay chuyển MP4.
- Hướng dẫn Huy từng bước để tự kiểm trên máy Windows, rồi cập nhật README.md.

Claude tự chạy thử phần chạy được trên Linux (kế hoạch dựng, FFmpeg, dựng đồ họa). Phần mở CapCut chỉ kiểm được trên máy Huy.

## 6. Tiêu chí nghiệm thu C1 (đề xuất, Huy sửa nếu muốn)

1. T4, T6, T11 đạt → **CapCut dùng được**, đi tiếp. Nếu một trong ba không đạt sau khi đã thử T5 → **chuyển sang MP4**.
2. T8 hoặc T9 đạt ít nhất một → chốt cách làm lớp phủ đồ họa.
3. T7 đạt → chữ tiếng Việt dùng được; không đạt thì ghi lại, không chặn C1.
4. T10 đạt → luôn có đường lùi MP4.
5. Có `docs/c1-ketqua.md` và README.md cập nhật.

## 7. Câu hỏi còn mở (cần Huy trả lời trước khi chạy)

1. Huy cho phép Claude điều khiển máy Windows (mở CapCut, chạy lệnh) để tự làm T1–T11, hay Huy muốn tự bấm theo hướng dẫn?
2. Python và FFmpeg đã có trên máy chưa? Nếu chưa, Claude cài giúp được không?
3. Thư mục để video thử: `C:\VideoBDS\test-c1\` được không, hay Huy chọn chỗ khác?

## 8. Ngoài phạm vi C1

Whisper, kịch bản, phiếu thông tin, 5 mẫu đồ họa thật, Google Drive, nhạc, logo, Skill cho chị: để các chặng sau.

**Thiếu thông tin:** chi tiết và tiêu chí nghiệm thu của C2–C7 bị mất khi xuất brief (xem ghi chú trong `docs/brief.md`). Claude chưa lập kế hoạch các chặng đó.
