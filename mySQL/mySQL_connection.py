import mysql.connector

# B1: Kết nối tới MySQL
conn = mysql.connector.connect(
    host="localhost",        # Máy chủ (nếu MySQL cài trên máy khác thì đổi IP)
    user="root",             # Tên đăng nhập MySQL
    password="Vietnam2025",  # Mật khẩu MySQL
    database="company_db"    # Tên database đã tạo
)

# B2: Tạo cursor để thao tác
cursor = conn.cursor()

# B3: Viết câu lệnh SQL
query = "SELECT * FROM employees;"

cursor.execute(query)

# B4: Lấy tất cả dữ liệu
rows = cursor.fetchall()

# B5: In dữ liệu ra màn hình
for row in rows:
    print(row)

# B6: Đóng kết nối
cursor.close()
conn.close()
