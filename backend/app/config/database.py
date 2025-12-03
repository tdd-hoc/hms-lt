from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import settings

# 1. Tạo Engine kết nối
# settings.SQLALCHEMY_DATABASE_URL lấy từ file settings.py
# pool_pre_ping=True: Giúp kiểm tra kết nối trước khi thực hiện truy vấn, 
# tránh lỗi "MySQL server has gone away" nếu kết nối bị ngắt.
engine = create_engine(
    settings.SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True
)

# 2. Tạo SessionLocal
# Đây là "nhà máy" để tạo ra các session (phiên làm việc) với database.
# Mỗi request sẽ dùng một session riêng biệt.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 3. Tạo Base class
# Tất cả các Models (Customer, Room, Booking...) sau này sẽ kế thừa từ class này.
Base = declarative_base()

# 4. Dependency (Hàm phụ thuộc)
# Hàm này sẽ được dùng trong các API (routers) để lấy kết nối DB.
# Sử dụng yield để đảm bảo kết nối được đóng lại (db.close()) sau khi xử lý xong request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()