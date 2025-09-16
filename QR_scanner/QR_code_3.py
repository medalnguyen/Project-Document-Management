from pdf2image import convert_from_path
import cv2
import pyzbar.pyzbar as pyzbar
# B1: Chuyển từng trang PDF thành ảnh
pages = convert_from_path(r"E:\Promgramming\BB_AQAT-94_AQAT-94-01_S-CC-DAC.pdf", dpi=300, poppler_path=r"C:\poppler-25.07.0\Library\bin")

for i, page in enumerate(pages):
    # Lưu tạm thành file ảnh
    filename = f"page_{i}.jpg"
    page.save(filename, "JPEG")

    # Đọc lại ảnh bằng OpenCV
    img = cv2.imread(filename)

    # B2: Giải mã QR trong ảnh
    decoded_objects = pyzbar.decode(img)

    # B3: Xuất kết quả
    for obj in decoded_objects:
        print("Page:", i+1)
        print("Type:", obj.type)
        print("Data:", obj.data.decode("utf-8"))