import cv2
import pyzbar.pyzbar as pyzbar

# Đọc ảnh chứa QR code
img = cv2.imread("QR_checksheet.jpg")

# Giải mã QR
decoded_objects = pyzbar.decode(img)

# In ra kết quả
for obj in decoded_objects:
    print("Type:", obj.type)   # Loại mã (QR_CODE, CODE128, v.v.)
    print("Data:", obj.data.decode("utf-8"))  # Nội dung giải mã
