import enum
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, Enum, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

class PaymentMethod(str, enum.Enum):
    Cash = "Cash"
    Momo = "Momo"
    VNPay = "VNPay"
    Visa = "Visa"
    MasterCard = "MasterCard"
    BankTransfer = "BankTransfer"

class PaymentStatus(str, enum.Enum):
    Pending = "Pending"
    Paid = "Paid"
    Failed = "Failed"

class Payment(Base):
    __tablename__ = "Payment"

    Payment_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Liên kết với Booking (Bắt buộc)
    Booking_ID = Column(Integer, ForeignKey('Booking.Booking_ID'), nullable=False)
    
    # Liên kết với Invoice (Có thể NULL nếu thanh toán cọc trước khi xuất hóa đơn)
    Invoice_ID = Column(Integer, ForeignKey('Invoice.Invoice_ID'), nullable=True)
    
    Method = Column(Enum(PaymentMethod), nullable=False)
    Amount = Column(DECIMAL(12, 2), nullable=False)
    Payment_Date = Column(DateTime, server_default=func.now())
    
    # Transaction ID từ cổng thanh toán (Momo/VNPay), Unique để tránh trùng lặp
    Transaction_ID = Column(String(100), unique=True, nullable=True)
    
    Status = Column(Enum(PaymentStatus), default=PaymentStatus.Paid)

    # --- Quan hệ ---
    booking = relationship("Booking", back_populates="payments")
    invoice = relationship("Invoice", back_populates="payments")