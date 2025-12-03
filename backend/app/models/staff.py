import enum
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

# Định nghĩa Enum cho Role để đảm bảo chỉ nhận các giá trị hợp lệ
class StaffRole(str, enum.Enum):
    Admin = "Admin"
    Receptionist = "Receptionist"
    Housekeeping = "Housekeeping"

class Staff(Base):
    __tablename__ = "Staff"

    Staff_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Name = Column(String(100), nullable=False)
    
    # Sử dụng Enum trong SQLAlchemy
    Role = Column(Enum(StaffRole), nullable=False)
    
    Email = Column(String(100), unique=True, nullable=False)
    Phone_Number = Column(String(20), nullable=True)
    Password_Hash = Column(String(255), nullable=False)
    Is_Active = Column(Boolean, default=True)
    Created_At = Column(DateTime, server_default=func.now())

    # --- Quan hệ (Relationships) ---
    # 1. Nhân viên tạo các Booking (Lễ tân)
    created_bookings = relationship("Booking", back_populates="creator_staff")

    # 2. Nhân viên ghi nhận các khoản phụ phí (Booking_Charge)
    recorded_charges = relationship("BookingCharge", back_populates="staff")

    # 3. Nhân viên thực hiện dọn phòng (Housekeeping)
    housekeeping_tasks = relationship("Housekeeping", back_populates="staff")

    # 4. Nhật ký hoạt động
    audit_logs = relationship("AuditLog", back_populates="staff")