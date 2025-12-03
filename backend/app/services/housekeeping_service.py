from sqlalchemy.orm import Session
from datetime import date

from app.models.room import Room, RoomStatus
from app.models.housekeeping import Housekeeping, HousekeepingStatus
from app.models.staff import Staff, StaffRole

class HousekeepingService:

    # 1. Tự động tạo task dọn phòng khi đổi trạng thái phòng sang 'Cleaning'
    def auto_generate_cleaning_task(self, db: Session, room_id: int, notes: str = "Auto-generated upon checkout"):
        # Tạo bản ghi nhiệm vụ mới
        new_task = Housekeeping(
            Room_ID=room_id,
            Task_Date=date.today(),
            Status=HousekeepingStatus.Pending,
            Notes=notes
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return new_task

    # 2. Gợi ý nhân viên rảnh rỗi để giao việc (Logic đơn giản: Lấy ngẫu nhiên nhân viên dọn phòng)
    # Trong thực tế có thể phức tạp hơn (VD: ai ít việc nhất thì giao)
    def suggest_available_housekeeper(self, db: Session):
        staff = db.query(Staff).filter(
            Staff.Role == StaffRole.Housekeeping,
            Staff.Is_Active == True
        ).first()
        return staff

    # 3. Đánh dấu phòng sạch sẽ sau khi dọn xong
    def mark_room_as_clean(self, db: Session, task_id: int):
        # Tìm task
        task = db.query(Housekeeping).filter(Housekeeping.Task_ID == task_id).first()
        if not task:
            return None
        
        # Cập nhật task thành Done
        task.Status = HousekeepingStatus.Done
        
        # Cập nhật trạng thái phòng thành Available
        room = db.query(Room).filter(Room.Room_ID == task.Room_ID).first()
        if room:
            room.Status = RoomStatus.Available
        
        db.commit()
        return task

housekeeping_service = HousekeepingService()