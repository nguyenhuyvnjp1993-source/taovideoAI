# Kế hoạch chặng C2: phiếu thông tin, 2 mẫu kịch bản, danh sách cảnh, luật cấm

Trạng thái: **chờ Huy duyệt**. Chưa viết code C2.

## 1. Mục tiêu của C2

Chị gõ "dựng căn mới", trả lời phiếu trong 1–2 phút, rồi nhận về:

1. **Kịch bản video dài** (3–5 phút) theo giọng của chị.
2. **Cách tách 2–3 video ngắn** (30–60 giây) từ chính lần quay đó.
3. **Danh sách cảnh cần quay theo thứ tự**, để quay một lượt.

Mọi câu chữ đi qua **bộ kiểm luật cấm** trước khi đưa cho chị. Thiếu ô nào trong phiếu thì Claude hỏi lại, không tự điền.

Theo trả lời của Huy: kịch bản chỉ là **khung gợi ý**, chị có thể nói khác khi quay. Thứ quan trọng nhất của C2 là **danh sách cảnh**, vì C3 dựa vào thứ tự cảnh để cắt video.

## 2. Chia việc: phần nào là code, phần nào Claude viết

| Phần | Ai làm | Lý do |
| --- | --- | --- |
| Phiếu thông tin: ô nào bắt buộc, kiểm thiếu ô, chuẩn hóa địa chỉ | **Code** (Python) | Phải chắc chắn, không được quên ô |
| Luật cấm: dò từ cấm, gợi ý câu thay, dòng cảnh báo bắt buộc | **Code** (Python) | Kiểm lặp lại được, không phụ thuộc trí nhớ của Claude |
| Viết kịch bản theo giọng chị | **Claude**, theo file hướng dẫn trong repo | Việc viết cần ngôn ngữ tự nhiên |
| Khung kịch bản và danh sách cảnh | **File mẫu** (Markdown + JSON) | Claude điền vào khung, code kiểm khung đủ phần |

Các file hướng dẫn này về sau đóng gói vào Skill ở C6.

## 3. Sản phẩm C2

### 3.1 Phiếu thông tin (`taovideo/phieu.py`, `mau/phieu_*.json`)

- 3 loại phiếu đúng bảng trong brief: **đất nền**, **nhà phố** (= đất nền + số tầng, số phòng, năm xây, nội thất), **NOXH**.
- Mỗi ô có: tên, bắt buộc hay không, kiểu (số, chữ, lựa chọn), đơn vị (m², m, km, triệu/tỷ).
- **Pháp lý là ô lựa chọn**, không gõ tự do: ví dụ "Sổ đỏ riêng", "Sổ chung", "Đang làm sổ", "Hợp đồng mua bán", "Khác (ghi rõ)". Chọn "Đang làm sổ" thì code cấm chữ "sổ đỏ" trong kịch bản.
- **Địa chỉ**: chị nhập xã/phường mới + tên cũ, code ghép thành "xã X, tỉnh Hưng Yên (Thái Bình cũ)". Tên huyện cũ đứng một mình bị báo lỗi.
- Hàm `kiem_phieu()` trả về danh sách ô còn thiếu hoặc sai kiểu, để Claude hỏi lại đúng ô đó.
- NOXH: giá Nhà nước duyệt, đối tượng được mua, lãi suất **bắt buộc do chị nhập**; thiếu thì ghi "cần kiểm tra", không tự điền.

### 3.2 Luật cấm (`taovideo/luat_cam.py`, `mau/luat_cam.json`)

- Danh sách lấy đúng bảng "Luật nội dung và pháp lý" trong brief, chia nhóm: NOXH, đất nền/nhà phố, lời văn, địa chỉ.
- Dò cả biến thể: viết hoa, không dấu ("sieu pham"), cách viết khác ("cơ hội vàng" / "cơ hội có một không hai" chỉ dò được nếu Huy thêm vào danh sách).
- Mỗi lỗi trả về: câu vi phạm, nhóm luật, **câu thay thế gợi ý**.
- Luật theo ngữ cảnh: "sổ đỏ" chỉ bị cấm khi phiếu không chọn "Sổ đỏ riêng"; "sắp lên quy hoạch" bị cấm trừ khi phiếu có ô "có văn bản quy hoạch".
- Dòng bắt buộc: video NOXH luôn có "thông tin tham khảo, điều kiện cụ thể theo quy định hiện hành"; bảng trả góp luôn có "Số liệu minh họa, lãi suất thực tế theo ngân hàng".
- **Kiểm con số**: mọi con số trong kịch bản phải có trong phiếu (giá, diện tích, mặt tiền, km…). Số không có trong phiếu bị báo lỗi.

### 3.3 Hai mẫu kịch bản (`mau/kich_ban_dan_xem.md`, `mau/kich_ban_tu_van.md`)

**Mẫu 1: dẫn đi xem một lô đất / căn nhà.** Khung video dài theo đúng thứ tự trong brief:

| Đoạn | Nội dung | Gợi ý thời lượng |
| --- | --- | --- |
| Mở | Câu mở: loại BĐS, vị trí, giá (1–2 câu) | 10–15 giây |
| Đường vào | Rộng bao nhiêu, ô tô vào được không | 30–45 giây |
| Mặt tiền | Mặt tiền, hướng, diện tích | 30–45 giây |
| Pháp lý | Đúng tình trạng đã chọn trong phiếu | 20–30 giây |
| Xung quanh | Chợ, trường, KCN, quốc lộ + km | 40–60 giây |
| (Nhà phố) Bên trong | Số tầng, phòng, năm xây, nội thất | 40–60 giây |
| Kết | Câu kết cố định + Zalo | 10 giây |

Mỗi đoạn dài là một **chương** (khớp mẫu "thẻ chương" trong `docs/motion.md`), và cũng là chỗ cắt ra video ngắn.

**Mẫu 2: tư vấn kiến thức** (pháp lý sổ đỏ, quy hoạch, kinh nghiệm mua, điều kiện NOXH): câu hỏi mở → 3 ý chính → ví dụ thực tế → câu kết. Với NOXH, mọi điều kiện và con số để trống cho chị điền hoặc ghi "cần kiểm tra".

**Tách video ngắn:** mỗi video ngắn = câu mở mới + 3 điểm nổi bật lấy từ các chương + câu kết. Claude chỉ ra video ngắn lấy từ giây nào của chương nào (C4 sẽ dùng).

**Giọng văn:** xưng "em", gọi "anh chị", câu ngắn (tối đa khoảng 15 chữ một câu để đọc trước máy không vấp), đi thẳng vào số liệu. Code đếm độ dài câu và báo câu quá dài.

**Câu kết cố định:** tên chị + số Zalo + "nhắn em để nhận video chi tiết và giấy tờ" (NOXH: "nhắn em để kiểm tra điều kiện mua"). Tên và số Zalo đọc từ `config.json`, không commit.

### 3.4 Danh sách cảnh (`taovideo/danh_sach_canh.py`)

- Xuất ra 2 dạng: **bản cho chị** (Markdown dễ đọc trên điện thoại: số cảnh, quay gì, nói gì, khoảng bao lâu) và **bản cho máy** (JSON: số cảnh, chương, câu thoại dự kiến, thời lượng).
- Mỗi cảnh quay thành **một file riêng**, theo đúng thứ tự, để C3 nhận ra cảnh theo thứ tự file.
- Ghi rõ cảnh nào cần video chủ nhà gửi (ví dụ cảnh bên trong khi chị không vào được).

### 3.5 Kiểm thử

- 3 phiếu mẫu (đất nền, nhà phố, NOXH) với **số liệu giả ghi rõ là giả**, cùng 2–3 phiếu cố tình thiếu ô.
- Bộ câu thử cho luật cấm: mỗi luật ít nhất 1 câu vi phạm và 1 câu hợp lệ (không báo nhầm).
- Claude viết thử 1 kịch bản cho mỗi phiếu mẫu, chạy qua bộ kiểm, đưa Huy đọc.

## 4. Tiêu chí nghiệm thu C2 (đề xuất, Huy sửa nếu muốn)

1. Phiếu thiếu ô nào thì code chỉ đúng ô đó; phiếu đủ thì qua.
2. Bộ kiểm luật cấm bắt được 100% câu vi phạm trong bộ câu thử, không báo nhầm câu hợp lệ.
3. Mọi con số trong kịch bản mẫu đều có trong phiếu.
4. Với mỗi phiếu mẫu có: kịch bản dài, cách tách 2–3 video ngắn, danh sách cảnh (bản cho chị + bản JSON).
5. **Huy đọc 3 kịch bản mẫu và thấy giọng gần với chị.** Đây là tiêu chí cảm tính, Huy quyết.
6. README.md cập nhật, giải thích lại C2 trong 3–5 câu.

## 5. Việc Huy chuẩn bị trước khi chạy C2 (theo brief)

| # | Việc | Dùng để |
| --- | --- | --- |
| P1 | **2–3 link video chị ưng nhất** | Claude học giọng, cách mở, cách kết |
| P2 | **1 video quay thô chưa cắt** | Xem chị nói thế nào khi chưa cắt, độ dài câu thật |
| P3 | Tên chị muốn hiện ở câu kết và số Zalo | Ghi vào `config.json` trên máy, không commit |
| P4 | (Không bắt buộc) 1 căn thật chị sắp quay, điền phiếu | Thử phiếu với dữ liệu thật |

Nếu chưa có P1–P2, Claude vẫn làm được phần phiếu, luật cấm và khung kịch bản; chỉ phần "giọng của chị" phải chờ.

## 6. Câu hỏi còn mở

1. Danh sách lựa chọn cho ô **pháp lý**: Claude đề xuất 5 lựa chọn ở mục 3.1, Huy hoặc chị sửa giúp cho đúng cách nói ở địa phương.
2. Giá ghi kiểu nào: "1,25 tỷ" hay "1 tỷ 250 triệu"? Có ghi giá theo m² không?
3. Video ngắn dạng "mẹo tư vấn" có cần làm luôn ở C2, hay chỉ tách từ video dài?

## 7. Ngoài phạm vi C2

Cắt video, Whisper (C3); chữ, nhạc, câu kết trên video (C4); đồ họa (C5); đóng gói Skill, Google Sheet (C6).
