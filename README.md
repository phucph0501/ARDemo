# AR Video (miễn phí, chạy trên web)

Giống tính năng **AR Video** như ar-code.com: quét **mã QR** → mở trang web → đưa camera đến **ảnh mục tiêu** (có thể chính là QR) → **video** hiển thị đè lên ảnh trong AR.

## 1) Chuẩn bị ảnh mục tiêu (image target)
- Chọn **ảnh tĩnh** bạn muốn nhận diện (ví dụ: chính **QR** in ra, poster, logo…).
- Dùng **MindAR Image Compiler** để tạo file `targets.mind` từ ảnh đó. Bạn có thể dùng tool dòng lệnh `mindar-image compile --input target.jpg --output targets.mind` (cài `mind-ar` bằng npm) hoặc dùng tool web của MindAR.
- Đặt `targets.mind` vào cùng thư mục với `index.html`.
- Tạo tại đây https://www.mindar.org/how-to-choose-a-good-target-image-for-tracking-in-ar-part-1/?utm_source=chatgpt.com
> Mẹo: Ảnh có **nhiều chi tiết**/texture sẽ theo dõi tốt hơn ảnh phẳng trơn.

## 2) Thêm video của bạn
- Đổi tên/đường dẫn `./video.mp4` trong `index.html` thành video của bạn.
- Nên dùng **MP4 H.264 + AAC**, càng nhẹ càng tốt để load nhanh (720p là ổn).

## 3) Chạy thử
- Mở `index.html` bằng một **web server** (không mở file://). Ví dụ dùng VSCode Live Server, `python -m http.server`, hoặc deploy Netlify/GitHub Pages/Vercel.
- Trên điện thoại, cấp quyền camera, đưa camera tới ảnh mục tiêu → video sẽ phát. Nhấn **Bật tiếng** để mở âm thanh (autoplay mặc định sẽ tắt tiếng).

## 4) Tạo mã QR
- Khi bạn đã có URL (ví dụ `https://tenban.github.io/ar-video-qr`), chạy `python generate_qr.py` và dán URL để tạo `qr.png` với một badge tròn "AR". In/sticker mã này.
- Khi quét QR, trang sẽ mở → đưa camera nhìn **ảnh mục tiêu** (chính QR hoặc poster) là video sẽ hiện.

## 5) Tùy chỉnh
- Kích thước video phủ trên ảnh được đặt ở `<a-video width="1" height="0.5625">` (tỉ lệ 16:9). Thay đổi theo tỉ lệ nội dung của bạn.
- Nếu muốn video **luôn phát** ngay cả khi mất marker, bỏ event `targetLost` trong `script.js`.

## 6) Cấu trúc
```
ar-video-qr/
├─ index.html
├─ script.js
├─ style.css
├─ targets.mind        ← tạo từ ảnh mục tiêu
├─ video.mp4           ← video của bạn
└─ generate_qr.py      ← tạo QR có badge "AR"
```

## Lưu ý bảo mật & quyền
- Video public ai có link đều xem được. Nếu cần riêng tư hơn, hãy tự host và kiểm soát truy cập.
