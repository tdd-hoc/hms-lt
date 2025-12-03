import enum
from sqlalchemy import Column, Integer, String, DECIMAL, Text, JSON, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

# Định nghĩa Enum cho trạng thái phòng
class RoomStatus(str, enum.Enum):
    Available = "Available"
    Booked = "Booked"
    Cleaning = "Cleaning"
    Maintenance = "Maintenance"

class Room(Base):
    __tablename__ = "Room"

    Room_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Room_Number = Column(String(20), unique=True, nullable=False)
    Room_Type = Column(String(50), nullable=False)
    
    # DECIMAL(12, 2) cho tiền tệ để tránh sai số thập phân
    Base_Price = Column(DECIMAL(12, 2), nullable=False)
    
    # Mặc định là 'Available'
    Status = Column(Enum(RoomStatus), default=RoomStatus.Available)
    
    Amenities = Column(Text, nullable=True)
    
    # Kiểu JSON của MySQL để lưu danh sách link ảnh: ["url1", "url2"]
    Image_URLs = Column(JSON, nullable=True)
    
    Created_At = Column(DateTime, server_default=func.now())

    # --- Quan hệ (Relationships) ---
    # 1. Một phòng có nhiều lịch sử Booking
    bookings = relationship("Booking", back_populates="room")

    # 2. Một phòng có nhiều lịch dọn dẹp
    housekeeping_tasks = relationship("Housekeeping", back_populates="room")