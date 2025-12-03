import enum
from sqlalchemy import Column, Integer, Date, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship
from ..config.database import Base

# Định nghĩa Enum cho trạng thái công việc dọn phòng
class HousekeepingStatus(str, enum.Enum):
    Pending = "Pending"         # Chờ xử lý
    InProgress = "InProgress"   # Đang dọn
    Done = "Done"               # Đã xong
    Canceled = "Canceled"       # Hủy bỏ

class Housekeeping(Base):
    __tablename__ = "Housekeeping"

    Task_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Phòng cần dọn (Bắt buộc)
    Room_ID = Column(Integer, ForeignKey('Room.Room_ID'), nullable=False)
    
    # Nhân viên được phân công (Có thể NULL nếu chưa giao việc)
    Staff_ID = Column(Integer, ForeignKey('Staff.Staff_ID'), nullable=True)
    
    # Ngày thực hiện
    Task_Date = Column(Date, nullable=False)
    
    # Ghi chú (VD: "Khách cần thêm khăn", "Hỏng bóng đèn")
    Notes = Column(Text, nullable=True)
    
    # Trạng thái công việc
    Status = Column(Enum(HousekeepingStatus), default=HousekeepingStatus.Pending)

    # --- Quan hệ (Relationships) ---
    
    # 1. Liên kết với Room
    # Để biết nhiệm vụ này thuộc phòng nào (room.Room_Number)
    room = relationship("Room", back_populates="housekeeping_tasks")

    # 2. Liên kết với Staff
    # Để biết ai là người chịu trách nhiệm (staff.Name)
    staff = relationship("Staff", back_populates="housekeeping_tasks")