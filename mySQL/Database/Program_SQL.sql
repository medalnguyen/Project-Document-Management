-- DROP DATABASE company_db;
-- CREATE DATABASE company_db;

-- USE company_db;

-- CREATE TABLE employees (
--     employee_id INT AUTO_INCREMENT PRIMARY KEY,     -- Khóa chính, tự động tăng
--     employee_code VARCHAR(10) NOT NULL UNIQUE,      -- Mã nhân viên (duy nhất)
--     full_name VARCHAR(100) NOT NULL,                -- Họ và tên
--     position VARCHAR(50) NOT NULL,                  -- Chức vụ
--     department VARCHAR(50) NOT NULL,                -- Phòng ban
--     company_email VARCHAR(100) NOT NULL UNIQUE,     -- Email công ty (duy nhất)
--     phone VARCHAR(15),                              -- Số điện thoại
--     hire_date DATE NOT NULL                         -- Ngày tuyển dụng
-- );

INSERT INTO employees (employee_code, full_name, position, department, company_email, phone, hire_date)
VALUES
 ('EMP001', 'Nguyen Van A', 'Commissioning Engineer', 'Commissioning', 'ng.vana@company.vn', '0123456789', '2022-05-10'),
 ('EMP002', 'Tran Thi B', 'Project Manager', 'Project', 'tt.b@company.vn', '0987654321', '2021-08-20');