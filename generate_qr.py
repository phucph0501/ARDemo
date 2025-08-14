import qrcode
from PIL import Image, ImageDraw, ImageFont
import io

url = input("Dán URL trang AR của bạn: ").strip()
if not url:
    raise SystemExit("URL rỗng. Thoát.")

# Tạo QR cơ bản
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # H để chèn logo/badge
    box_size=12,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

# Vẽ badge tròn "AR"
W, H = img.size
badge_d = int(min(W, H) * 0.22)  # đường kính badge
badge = Image.new("RGBA", (badge_d, badge_d), (0, 0, 0, 0))
draw = ImageDraw.Draw(badge)
draw.ellipse((0, 0, badge_d-1, badge_d-1), fill=(132, 234, 167, 255))  # xanh lá nhạt

# Chữ "AR" ở giữa
try:
    font = ImageFont.truetype("arial.ttf", int(badge_d * 0.42))
except:
    font = ImageFont.load_default()
text = "AR"
tw, th = draw.textsize(text, font=font)
draw.text(((badge_d - tw) / 2, (badge_d - th) / 2), text, fill=(0,0,0,255), font=font)

# Dán badge vào giữa QR
img.paste(badge, ((W - badge_d)//2, (H - badge_d)//2), badge)

out_path = "qr.png"
img.save(out_path)
print(f"Đã tạo {out_path}. Hãy thử quét để kiểm tra URL.")
