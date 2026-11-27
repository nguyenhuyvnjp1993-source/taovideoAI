# Brief dự án video BĐS (Claude + CapCut)

Nov 27, 2026 · @グェン　ゴック　フィ

## Mục tiêu và người dùng

Dự án giúp chị của Huy rút thời gian làm video BĐS từ nhiều giờ xuống còn khoảng 10–15 phút chỉnh sửa cho mỗi video: Claude viết kịch bản, cắt clip, vẽ đồ họa và xuất sẵn file dự án CapCut bản máy tính (JSON).

- **Người dùng:** chị của Huy, môi giới và tư vấn BĐS, không rành công nghệ. Hiện chị quay bằng điện thoại và tự cắt trên CapCut, khâu này tốn nhiều thời gian nhất.
- **Người dựng và bảo trì:** Huy giao việc và nghiệm thu, Claude Code viết code, Huy đóng gói quy trình thành một Skill để chị tự dùng.
- **Khâu đang tốn thời gian:** nghĩ nội dung, quay đi quay lại, cắt ghép, gõ chữ và phụ đề.
- **Nguyên tắc:** Claude dựng khung, chị hoàn thiện. Không nhắm tới dựng tự động 100%.

## Thị trường, loại BĐS, khách hàng

Chị làm BĐS ở Hưng Yên, Thái Bình cũ và các tỉnh lân cận, video hoàn toàn bằng tiếng Việt.

- **Địa giới hành chính:** từ ngày 1/7/2025 Thái Bình đã sáp nhập vào tỉnh Hưng Yên và cấp huyện bị bỏ. Địa chỉ ghi theo tên mới, kèm tên cũ, ví dụ “xã X, tỉnh Hưng Yên (Thái Bình cũ)”.
- **Loại BĐS:** đất nền, nhà phố, nhà ở xã hội (NOXH).
- **Khách hàng:** người địa phương mua để ở, nhà đầu tư từ Hà Nội, người làm ăn xa gửi tiền về mua, công nhân khu công nghiệp (chủ yếu NOXH). Người ở xa không về xem được, nên cần video kỹ và rõ pháp lý nhất.
- **Kênh đăng:** ưu tiên Facebook Reels, sau đó TikTok và YouTube Shorts; khách nhắn qua Zalo.

## Định dạng video và mẫu nội dung

Mọi video quay dọc 9:16. Mỗi lần đi quay một căn ra 1 video dài và 2–3 video ngắn, tổng 3 video mỗi tuần lúc đầu.

| Loại | Độ dài | Vai trò | Nội dung |
| --- | --- | --- | --- |
| Video dài | 3–5 phút | Chốt khách đã quan tâm, nhất là người ở xa | Dẫn đi xem chi tiết: đường vào, mặt tiền, sổ, xung quanh |
| Video ngắn | 30–60 giây | Kéo người mới biết đến chị | Câu mở + 3 điểm nổi bật, hoặc một mẹo tư vấn |

**Hai mẫu kịch bản làm trước:**

1. Dẫn đi xem một lô đất hoặc căn nhà cụ thể.
2. Tư vấn kiến thức: pháp lý sổ đỏ, quy hoạch, kinh nghiệm mua, điều kiện NOXH.

**Giọng văn:** chị xưng “em”, gọi “anh chị”, gần gũi và đi thẳng vào thông tin. Không dùng “siêu phẩm, cơ hội vàng, duy nhất”. Câu ngắn để chị đọc trước máy quay không vấp. Claude học giọng từ 2–3 video cũ của chị.

**Câu kết cố định:** tên chị + số Zalo + “nhắn em để nhận video chi tiết và giấy tờ”, số Zalo hiện 3 giây cuối. Video NOXH kết bằng “nhắn em để kiểm tra điều kiện mua”.

**Nguồn hình:** video chị tự quay và video chủ nhà gửi. Không dùng AI để tạo hình căn nhà.

## Quy trình hằng ngày của chị

Chị chỉ làm 4 việc: trả lời phiếu, quay, đưa video vào máy, sửa và xuất. Còn lại Claude làm.

1. **Chị:** mở Claude Desktop, gõ “dựng căn mới”, trả lời phiếu thông tin (gõ hoặc đọc, 1–2 phút). Thiếu ô nào Claude hỏi lại, không tự bịa.
2. **Claude:** viết kịch bản video dài, chỉ ra cách tách 2–3 video ngắn, và đưa danh sách cảnh cần quay theo thứ tự.
3. **Chị:** quay một lượt theo đúng thứ tự cảnh, video lên Google Drive vào thư mục `Video-Can-Moi`. Video chủ nhà gửi qua Zalo lưu dạng File vào cùng thư mục.
4. **Claude (Cowork trên laptop):**
   - xác nhận bảng tất cả con số với chị một lần;
   - dùng Whisper offline để cắt khoảng lặng và đoạn nói vấp;
   - nhận biết cảnh theo thứ tự file, trích khung hình cho video chủ nhà gửi;
   - vẽ đồ họa chuyển động;
   - tạo file dự án CapCut: clip đã cắt, chữ tiêu đề và giá, chữ thông tin, đồ họa, nhạc, logo, câu kết có số Zalo;
   - chuyển video đã dùng sang thư mục lưu trữ của căn đó.
5. **Chị:** mở CapCut trên laptop, bấm phụ đề tự động, sửa 10–15 phút, xuất MP4, gửi sang điện thoại để đăng. Không đồng bộ dự án sang CapCut điện thoại (cần Pro).
6. **Chị:** khách nhắn tin thì hỏi “anh chị biết em qua video nào ạ?”, ghi vào Google Sheet. Mỗi tháng Claude đọc bảng và gợi ý loại video nên làm thêm.

**Phiếu thông tin theo loại:**

| Loại | Các ô bắt buộc |
| --- | --- |
| Đất nền | Vị trí (xã/phường mới + tên cũ), diện tích, mặt tiền, hướng, đường vào (rộng, ô tô vào được không), pháp lý, giá, điểm nổi bật, xung quanh (chợ, trường, KCN, quốc lộ + km) |
| Nhà phố | Như đất nền, thêm số tầng, số phòng, năm xây, nội thất |
| NOXH | Tên dự án, chủ đầu tư, giá Nhà nước duyệt, diện tích căn, tiến độ, đối tượng được mua, lãi suất vay (chị nhập) |

## Kiến trúc kỹ thuật

Toàn bộ chạy offline trên một laptop Windows, đóng gói thành Skill (hoặc plugin) cho Claude Desktop chế độ Cowork. Code nằm trong một repo GitHub mới, tách khỏi `homnayangi`.

| Thành phần | Chọn | Ghi chú |
| --- | --- | --- |
| Máy | Windows 11, RAM 16GB, SSD trống ≥ 100GB | Chạy cùng lúc CapCut, Claude Desktop, Whisper |
| CapCut | Bản máy tính 9.5, khóa bản, chặn tự cập nhật | Bản 10.x báo file do code tạo là hỏng |
| Tạo file dự án | pyCapCut 0.0.4 (khóa bản) | Đã thử trên CapCut 8.2 và 9.5; dự phòng: VectCutAPI |
| Nhận dạng giọng nói | Whisper offline | Miễn phí, không gửi video ra ngoài; máy chậm thì chỉ cắt khoảng lặng |
| Đồ họa | HTML/CSS/SVG, dựng thành clip bằng trình duyệt ẩn | Chèn vào lớp phủ trong CapCut |
| Dự phòng video | FFmpeg | Xuất MP4 bản nháp + phụ đề khi CapCut không mở được file |
| Chuyển video | Google Drive, thư mục `Video-Can-Moi` | Mỗi căn một thư mục lưu trữ sau khi dựng |

**Hai lớp, tách rời:**

- **Lớp lõi** không phụ thuộc CapCut: tạo “kế hoạch dựng” gồm clip nào, cắt từ giây nào đến giây nào, chữ gì, đồ họa gì, nhạc gì.
- **Lớp xuất** đọc kế hoạch đó và ghi ra file dự án CapCut, hoặc ra MP4 bản nháp bằng FFmpeg.

**Những điểm phải kiểm chứng ở C1:**

- Cowork trên Windows có ghi được vào thư mục dự án của CapCut và chạy được FFmpeg, Whisper, Python không.
- File dự án nên dựa trên một dự án thật tạo bằng tay trên đúng máy đó. Dự án phải được đăng ký với CapCut (`root_meta_info.json`), sau đó thoát hẳn CapCut rồi mở lại.
- Đường dẫn video ghi trong JSON phải là đường dẫn Windows thật trên máy, không phải đường dẫn trong môi trường Cowork.

## Đồ họa chuyển động

Lúc đầu chỉ có 5 mẫu, dùng lại cho mọi video. Claude viết mẫu bằng HTML/CSS/SVG, dựng thành clip, rồi đặt vào lớp phủ CapCut đúng giây cần hiện. Chị vẫn kéo, sửa, xóa được.

| # | Mẫu | Kiểu | Dữ liệu lấy từ phiếu |
| --- | --- | --- | --- |
| 1 | Thẻ giá và diện tích, số chạy từ 0 lên | Lớp phủ nhỏ | Giá, diện tích |
| 2 | Hàng icon thông số | Lớp phủ nhỏ | Hướng, mặt tiền, đường vào, pháp lý |
| 3 | Danh sách pháp lý có dấu tích | Lớp phủ hoặc thẻ | Chỉ các ô chị đã xác nhận |
| 4 | Sơ đồ khoảng cách (vẽ đơn giản, không dùng ảnh Google Maps) | Thẻ toàn màn hình 3–5 giây | KCN, chợ, trường, quốc lộ + km |
| 5 | Bảng chi phí hoặc trả góp | Thẻ toàn màn hình 3–5 giây | Giá, số tiền vay, lãi suất do chị nhập |

- **Con số:** chỉ hiện số có trong phiếu thông tin, Claude không tự tính hay ước lượng. Bảng trả góp luôn kèm dòng “Số liệu minh họa, lãi suất thực tế theo ngân hàng”.
- **Nền trong suốt:** lớp phủ nhỏ cần video nền trong suốt. Chưa chắc CapCut 9.5 nhận được, nên C1 sẽ kiểm tra. Nếu không nhận thì dựng trên nền xanh lá và file dự án tự bật xóa phông xanh.
- **Bộ nhận diện:** 1 màu chính + 1 màu phụ (theo logo của chị, hoặc chọn từ 2–3 phương án Claude đề xuất), font Be Vietnam Pro, icon Lucide hoặc Tabler, logo + tên + số Zalo ở góc. Tất cả nằm trong một file cấu hình: sửa một chỗ, mọi mẫu đổi theo.

## Luật nội dung và pháp lý

Gặp những câu dưới đây, Claude từ chối hoặc cảnh báo rồi đề xuất cách nói thay thế. Luật NOXH thay đổi thường xuyên, nên Claude không tự khẳng định điều kiện hay con số: chị phải điền, hoặc Claude ghi “cần kiểm tra”.

| Nhóm | Không được nói | Thay bằng |
| --- | --- | --- |
| NOXH | “Bán suất”, “suất ngoại giao”, giá chênh so với giá Nhà nước duyệt, “cam kết được duyệt”, “không cần chứng minh thu nhập”, chào bán lại căn chưa đủ thời hạn | Tư vấn điều kiện và hỗ trợ hồ sơ, kèm dòng “thông tin tham khảo, điều kiện cụ thể theo quy định hiện hành” |
| Đất nền, nhà phố | “Cam kết lãi X%”, “chắc chắn tăng giá”, “sắp lên quy hoạch” khi không có văn bản, gọi “sổ đỏ” khi chưa có sổ, giấu quy hoạch hoặc hành lang an toàn | Nêu đúng tình trạng pháp lý chị đã chọn trong phiếu (ô bắt buộc) |
| Lời văn | “Siêu phẩm”, “cơ hội vàng”, “duy nhất” | Thông tin cụ thể: số mét, km, giá |
| Địa chỉ | Tên huyện cũ đứng một mình | Tên xã/phường và tỉnh mới, kèm tên cũ trong ngoặc |
| Nhạc | Nhạc đang thịnh hành trên TikTok | 5–10 bài nhạc thương mại (CapCut Commercial hoặc kho miễn phí bản quyền) do Huy duyệt |
| Hình ảnh | Căn nhà do AI tạo ra | Chỉ video quay thật; sơ đồ vẽ tay thay ảnh chụp bản đồ |

## Rủi ro và dự phòng

Rủi ro lớn nhất là CapCut đổi định dạng file dự án. Quy trình phải tiếp tục chạy được kể cả khi CapCut ngừng mở file.

| Rủi ro | Dấu hiệu | Cách xử lý |
| --- | --- | --- |
| CapCut tự cập nhật lên 10.x | CapCut báo file dự án bị hỏng | Khóa bản 9.5, chặn cập nhật khi cài máy, sao lưu thư mục dự án lên Drive mỗi tuần |
| CapCut không mở được file vì lý do khác | Dự án không hiện hoặc mất clip | Xuất MP4 bản nháp + phụ đề (FFmpeg) từ cùng kế hoạch dựng |
| pyCapCut đổi giao diện ở bản 0.1.0 | Lỗi khi cài lại | Khóa pyCapCut 0.0.4; cần tính năng mới thì xem VectCutAPI |
| Điều khoản CapCut cấm script tự động (nguồn thứ cấp, chưa kiểm trên trang gốc) | CapCut chặn file kiểu này | Code chỉ ghi file lên ổ đĩa, không đăng nhập, không điều khiển app, không tự đăng. Huy đã chấp nhận rủi ro này; nếu bị chặn thì chuyển sang MP4 |
| Video nền trong suốt không nhập được | Lớp phủ có nền đen | Nền xanh lá + xóa phông xanh trong CapCut |
| Laptop chậm, Whisper lâu | Video 5 phút xử lý quá lâu | Chỉ cắt khoảng lặng, chưa cắt đoạn nói vấp |
| Con số sai trên đồ họa | Khách phát hiện sai, mất uy tín | Chỉ dùng số trong phiếu, chị xác nhận bảng số trước khi dựng |
| Zalo nén video chủ nhà gửi | Video mờ | Gửi và lưu dạng File, không phải dạng video |

## Các chặng và tiêu chí nghiệm thu

Mỗi phiên làm một chặng, lên kế hoạch trước và chờ Huy duyệt. C1 chạy trên máy Huy vì máy đã đủ cấu hình; C7 mới chuyển sang máy chị.

| Chặng | Nội dung |
| --- | --- |
| C1 | Thử trên máy bạn: bản CapCut, một file dự án có 3 clip và 1 dòng chữ, và thử clip nền trong suốt hoặc nền xanh |
| C2 | Phiếu thông tin, 2 mẫu kịch bản, danh sách cảnh, luật cấm |
| C3 | Cắt video theo cảnh và lời nói, xuất 1 video dài |
| C4 | Tách video ngắn, thêm chữ, nhạc và câu kết |
| C5 | Bộ nhận diện và 5 mẫu đồ họa chuyển động |
| C6 | Bản MP4 dự phòng, đóng gói Skill, hướng dẫn cho chị, bảng Sheet |
| C7 | Chuyển sang máy chị và chạy thử một căn thật |

> Bảng trên do Huy dán lại ngày 27/11/2026 (bản xuất gốc bị mất bảng này). Tiêu chí nghiệm thu riêng của từng chặng C2–C7 chưa có; sẽ đề xuất khi lập kế hoạch chặng đó. Kế hoạch C1 xem [docs/c1-plan.md](c1-plan.md).

**Điểm quyết định sau C1 (Huy chốt 27/11/2026):** thử với các bản CapCut hiện có. Nếu sau 2 ngày thử không tìm ra cách để CapCut mở được file dự án, chuyển sang xuất MP4.

Nếu C1 không mở được file dự án trên bản CapCut nào (hạn 2 ngày thử), dự án chuyển hẳn sang xuất MP4 trước khi tốn công làm các chặng sau. Tiêu chí nghiệm thu là đề xuất, Huy sửa trực tiếp nếu muốn.

## Việc Huy chuẩn bị và CLAUDE.md mẫu

Mỗi chuẩn bị gắn với chặng cần nó. Chưa xong thì chặng đó chưa bắt đầu.

- [ ] Trước C1: xem máy Huy đang chạy CapCut bản nào; nếu là 10.x thì gỡ và cài bản 9.5
- [ ] Trước C1: chuẩn bị 3 clip ngắn quay dọc bất kỳ để thử
- [ ] Trước C2: 2–3 link video chị ưng nhất + 1 video quay thô chưa cắt
- [ ] Trước C4: danh sách 5–10 bài nhạc thương mại
- [ ] Trước C5: logo hoặc màu chị hay dùng (nếu có)
- [ ] Trước C7: cấu hình laptop của chị (hoặc mua máy Windows 11, RAM 16GB, SSD ≥ 100GB trống)

**Cách dùng tài liệu này trong project mới:** tạo repo mới, lưu tài liệu này thành `docs/brief.md` (xuất ra Markdown), dán khối dưới đây vào `CLAUDE.md`, rồi nói “bắt đầu C1”.

```markdown
# Video BĐS cho chị (Claude + CapCut)

## Người dùng và cách làm việc
- Chủ dự án: Huy (kỹ sư BIM, không biết lập trình). Huy giao việc và nghiệm thu, Claude viết code.
- Người dùng cuối: chị của Huy, môi giới BĐS, không rành công nghệ.
- Trả lời bằng tiếng Việt.
- Mỗi phiên làm MỘT chặng (xem docs/brief.md). Lên kế hoạch trước, chờ Huy duyệt rồi mới viết code.
- Trước khi báo xong: tự chạy thử, rồi chỉ Huy cách kiểm trên máy Windows thật có CapCut 9.5.
- Xong mỗi chặng: giải thích lại trong 3–5 câu và cập nhật README.md.
- Không tự thêm tính năng ngoài brief.

## Luật cố định
- CapCut bản máy tính 9.5 trên Windows, pyCapCut 0.0.4. Không nâng bản khi chưa được Huy duyệt.
- Lớp lõi (kế hoạch dựng) tách khỏi lớp xuất (CapCut JSON / MP4 FFmpeg).
- Đồ họa và kịch bản chỉ dùng con số trong phiếu thông tin. Không tự bịa.
- Tuân thủ mục “Luật nội dung và pháp lý” trong docs/brief.md.
- Không đưa khóa, mật khẩu hay số điện thoại cá nhân vào code hoặc commit; số Zalo nằm trong file cấu hình không commit.

## Chặng
- C1 đến C7: xem docs/brief.md, mục “Các chặng”.
```
