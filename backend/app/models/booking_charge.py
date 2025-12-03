from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

class BookingCharge(Base):
    __tablename__ = "Booking_Charge"

    Charge_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Khóa ngoại liên kết với Booking (Bắt buộc)
    # Nếu xóa Booking -> Xóa luôn các charge liên quan (nhờ cài đặt DB cascade)
    Booking_ID = Column(Integer, ForeignKey('Booking.Booking_ID'), nullable=False)
    
    # Mô tả dịch vụ (Ví dụ: "Coca Cola x2", "Laundry Service")
    Description = Column(String(255), nullable=False)
    
    # Số tiền (Sử dụng DECIMAL cho tiền tệ)
    Amount = Column(DECIMAL(12, 2), nullable=False)
    
    # Thời gian ghi nhận
    Charge_Date = Column(DateTime, server_default=func.now())
    
    # Nhân viên ghi nhận khoản phí này (Có thể NULL nếu hệ thống tự động)
    Staff_Recorded_ID = Column(Integer, ForeignKey('Staff.Staff_ID'), nullable=True)

    # --- Quan hệ (Relationships) ---
    
    # 1. Liên kết ngược lại với Booking
    # Giúp truy cập: charge.booking.Room_Number...
    booking = relationship("Booking", back_populates="charges")

    # 2. Liên kết với Staff
    # Giúp truy cập: charge.staff.Name (Ai là người tính tiền này?)
    staff = relationship("Staff", back_populates="recorded_charges")