from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

class Customer(Base):
    __tablename__ = "Customer"

    # --- Các cột (Columns) khớp với bảng SQL ---
    Customer_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    Surname = Column(String(100), nullable=True)
    Phone_Number = Column(String(20), nullable=True)
    Address = Column(String(255), nullable=True)
    Age = Column(Integer, nullable=True)
    Postal_Code = Column(String(20), nullable=True)
    
    # Email là Unique và Index để tìm kiếm nhanh khi đăng nhập
    Email = Column(String(100), unique=True, index=True, nullable=True)
    
    Gender = Column(String(10), nullable=True)
    
    # Password_Hash lưu chuỗi mã hóa
    Password_Hash = Column(String(255), nullable=True)
    
    # server_default=func.now() tương đương DEFAULT CURRENT_TIMESTAMP trong SQL
    Created_At = Column(DateTime, server_default=func.now())

    # --- Quan hệ (Relationships) ---
    # Các dòng này không tạo cột trong DB, nhưng giúp Python truy vấn liên kết
    
    # 1 Khách hàng có nhiều Booking. 
    # 'Booking' là tên class Model (sẽ tạo sau), 'customer' là tên biến trong class Booking
    bookings = relationship("Booking", back_populates="customer")

    # 1 Khách hàng có nhiều dòng nhật ký (Audit Logs)
    audit_logs = relationship("AuditLog", back_populates="customer")