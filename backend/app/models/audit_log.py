from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..config.database import Base

class AuditLog(Base):
    __tablename__ = "Audit_Log"

    Log_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Người thực hiện hành động (Nhân viên HOẶC Khách hàng)
    Staff_ID = Column(Integer, ForeignKey('Staff.Staff_ID'), nullable=True)
    Customer_ID = Column(Integer, ForeignKey('Customer.Customer_ID'), nullable=True)
    
    # Hành động (VD: "CREATE_BOOKING", "UPDATE_ROOM_STATUS")
    Action = Column(String(255), nullable=False)
    
    # Lưu giá trị cũ/mới dưới dạng JSON: {"old_value": "A", "new_value": "B"}
    Details = Column(JSON, nullable=True)
    
    Timestamp = Column(DateTime, server_default=func.now())

    # --- Quan hệ ---
    staff = relationship("Staff", back_populates="audit_logs")
    customer = relationship("Customer", back_populates="audit_logs")