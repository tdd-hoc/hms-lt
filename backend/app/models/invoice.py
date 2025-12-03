import enum
# SỬA DÒNG IMPORT: as DateType
from sqlalchemy import Column, Integer, DECIMAL, Date as DateType, Enum, ForeignKey 
from sqlalchemy.orm import relationship
from ..config.database import Base

class InvoiceStatus(str, enum.Enum):
    Unpaid = "Unpaid"
    Partial = "Partial"
    Paid = "Paid"
    Canceled = "Canceled"

class Invoice(Base):
    __tablename__ = "Invoice"

    Invoice_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    Booking_ID = Column(Integer, ForeignKey('Booking.Booking_ID'), unique=True, nullable=True)
    
    Price = Column(DECIMAL(12, 2), nullable=False)
    Charges_Total = Column(DECIMAL(12, 2), default=0.00)
    Discount_Total = Column(DECIMAL(12, 2), default=0.00)
    Tax = Column(DECIMAL(12, 2), nullable=False)
    Total = Column(DECIMAL(12, 2), nullable=False)
    
    # SỬA DÒNG NÀY: Dùng DateType thay vì Date
    Date = Column(DateType, nullable=False)
    Due_Date = Column(DateType, nullable=True)
    
    Status = Column(Enum(InvoiceStatus), default=InvoiceStatus.Unpaid, name="payment_status")

    booking = relationship("Booking", back_populates="invoice")
    payments = relationship("Payment", back_populates="invoice")