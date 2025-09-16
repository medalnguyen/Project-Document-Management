from pdf2image import convert_from_path
import cv2
import pyzbar.pyzbar as pyzbar
import os

def extract_qr_from_pdf(pdf_paths):
    for pdf_path in pdf_paths:
        print(f"Processing file: {pdf_path}")
        page_number = 1
        for page in convert_from_path(pdf_path, dpi=300, poppler_path=r"C:\poppler-25.07.0\Library\bin"):
            # Lưu tạm thành file ảnh
            filename = "temp_page.jpg"
            page.save(filename, "JPEG")

            # Đọc lại ảnh bằng OpenCV
            img = cv2.imread(filename)

            # Giải mã QR trong ảnh
            decoded_objects = pyzbar.decode(img)

            # Xuất kết quả
            for obj in decoded_objects:
                print(f"Page: {page_number}")
                print("Type:", obj.type)
                print("Data:", obj.data.decode("utf-8"))
            page_number += 1

if __name__ == "__main__":
    folder_path = r"D:\Promgramming\QR_path"  # Thay đổi đường dẫn tới thư mục chứa các file PDF
    pdf_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
    extract_qr_from_pdf(pdf_paths)