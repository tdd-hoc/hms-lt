from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.config.database import get_db
from app.crud import housekeeping_crud, room_crud
from app.schemas.housekeeping_schema import HousekeepingCreate, HousekeepingUpdate, HousekeepingResponse
from app.models.housekeeping import HousekeepingStatus

router = APIRouter(prefix="/housekeeping", tags=["Housekeeping"])

# 1. Lấy danh sách nhiệm vụ (Có lọc: theo nhân viên, theo ngày, trạng thái...)
@router.get("/", response_model=List[HousekeepingResponse])
def read_tasks(
    skip: int = 0, 
    limit: int = 100,
    staff_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[HousekeepingStatus] = None,
    task_date: Optional[date] = None,
    db: Session = Depends(get_db)
):
    return housekeeping_crud.get_tasks(
        db, skip=skip, limit=limit,
        staff_id=staff_id, room_id=room_id, status=status, task_date=task_date
    )

# 2. Phân công dọn phòng
@router.post("/", response_model=HousekeepingResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: HousekeepingCreate, db: Session = Depends(get_db)):
    room = room_crud.get_room(db, room_id=task.Room_ID)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return housekeeping_crud.create_task(db, task)

# 3. Cập nhật trạng thái (VD: Nhân viên bấm "Done")
@router.put("/{task_id}", response_model=HousekeepingResponse)
def update_task(task_id: int, task_in: HousekeepingUpdate, db: Session = Depends(get_db)):
    db_task = housekeeping_crud.update_task(db, task_id, task_in)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task