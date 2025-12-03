import enum
from sqlalchemy import Column, Integer, String, DECIMAL, Date, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

# Định nghĩa Enum cho trạng thái đặt phòng
class BookingStatus(str, enum.Enum):
    Reserved = "Reserved"
    Confirmed = "Confirmed"
    Cancelled = "Cancelled"
    CheckedIn = "CheckedIn"
    CheckedOut = "CheckedOut"
    NoShow = "NoShow"

class Booking(Base):
    __tablename__ = "Booking"

    Booking_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Khóa ngoại 1: Liên kết với Khách hàng (có thể NULL nếu Lễ tân đặt hộ)
    Customer_ID = Column(Integer, ForeignKey('Customer.Customer_ID'), nullable=True)
    
    # Khóa ngoại 2: Liên kết với Phòng (KHÔNG được NULL)
    Room_ID = Column(Integer, ForeignKey('Room.Room_ID'), nullable=False)
    
    Checkin_Date = Column(Date, nullable=False)
    Checkout_Date = Column(Date, nullable=False)
    
    Status = Column(Enum(BookingStatus), default=BookingStatus.Reserved)
    
    # Lưu chi tiết tính giá (giảm giá, phụ phí tạm tính...)
    Calculated_Price_Details = Column(JSON, nullable=True)
    Total_Amount = Column(DECIMAL(12, 2), nullable=True)

    # Khóa ngoại 3: Nhân viên đã tạo booking này (có thể NULL nếu khách tự đặt)
    Created_By_Staff_ID = Column(Integer, ForeignKey('Staff.Staff_ID'), nullable=True)
    
    Created_At = Column(DateTime, server_default=func.now())
    
    # Tương đương với ON UPDATE CURRENT_TIMESTAMP trong MySQL
    Updated_At = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # --- Quan hệ (Relationships) ---
    
    # Quan hệ 1: Customer (từ bảng Customer)
    customer = relationship("Customer", back_populates="bookings")
    
    # Quan hệ 2: Room (từ bảng Room)
    room = relationship("Room", back_populates="bookings")

    # Quan hệ 3: Staff (Nhân viên tạo Booking - từ bảng Staff)
    creator_staff = relationship("Staff", back_populates="created_bookings")
    
    # Quan hệ N: Booking là cha của Payments (Một booking có nhiều lần thanh toán)
    payments = relationship("Payment", back_populates="booking")

    # Quan hệ N: Booking là cha của Charges (Một booking có nhiều phụ phí)
    charges = relationship("BookingCharge", back_populates="booking")
    
    # Quan hệ 1: Booking có một Invoice (Nếu Invoice.Booking_ID là UNIQUE)
    invoice = relationship("Invoice", back_populates="booking", uselist=False)