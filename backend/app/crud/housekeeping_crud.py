from sqlalchemy.orm import Session
from typing import Optional
from datetime import date
from app.models.housekeeping import Housekeeping, HousekeepingStatus
from app.schemas.housekeeping_schema import HousekeepingCreate, HousekeepingUpdate

# 1. Lấy nhiệm vụ theo ID
def get_task(db: Session, task_id: int):
    return db.query(Housekeeping).filter(Housekeeping.Task_ID == task_id).first()

# 2. Lấy danh sách nhiệm vụ (Hỗ trợ lọc đa dạng)
def get_tasks(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    staff_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[HousekeepingStatus] = None,
    task_date: Optional[date] = None
):
    query = db.query(Housekeeping)
    
    if staff_id:
        query = query.filter(Housekeeping.Staff_ID == staff_id)
    if room_id:
        query = query.filter(Housekeeping.Room_ID == room_id)
    if status:
        query = query.filter(Housekeeping.Status == status)
    if task_date:
        query = query.filter(Housekeeping.Task_Date == task_date)
        
    return query.offset(skip).limit(limit).all()

# 3. Tạo nhiệm vụ dọn phòng mới
def create_task(db: Session, task: HousekeepingCreate):
    db_task = Housekeeping(
        Room_ID=task.Room_ID,
        Staff_ID=task.Staff_ID, # Có thể Null
        Task_Date=task.Task_Date,
        Notes=task.Notes,
        Status=task.Status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 4. Cập nhật nhiệm vụ (Phân công nhân viên, đổi trạng thái Done)
def update_task(db: Session, task_id: int, task_update: HousekeepingUpdate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_task, key, value)
        
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# 5. Xóa nhiệm vụ
def delete_task(db: Session, task_id: int):
    db_task = get_task(db, task_id)
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task