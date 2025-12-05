# backend/Dockerfile

# 1. Sử dụng Python image nhẹ
FROM python:3.10-slim

# 2. Thiết lập thư mục làm việc
WORKDIR /app

# 3. Cài đặt các thư viện hệ thống cần thiết (để cài mysql-connector)
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# 4. Copy requirements và cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy toàn bộ code vào container
COPY . .

# 6. Mở port 8000
EXPOSE 80

# 7. Lệnh chạy server
CMD ["python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]