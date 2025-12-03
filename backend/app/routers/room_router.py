from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.crud import room_crud
from app.schemas.room_schema import RoomCreate, RoomUpdate, RoomResponse
from app.models.room import RoomStatus

router = APIRouter(
    prefix="/rooms",
    tags=["Rooms"]
)

# 1. Lấy danh sách phòng (Có thể lọc theo trạng thái Available)
# VD: GET /api/v1/rooms?status=Available
@router.get("/", response_model=List[RoomResponse])
def read_rooms(
    skip: int = 0, 
    limit: int = 100, 
    status: Optional[RoomStatus] = None, 
    db: Session = Depends(get_db)
):
    return room_crud.get_rooms(db, skip=skip, limit=limit, status=status)

# 2. Tạo phòng mới (Admin)
@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
def create_new_room(room: RoomCreate, db: Session = Depends(get_db)):
    # Kiểm tra số phòng trùng lặp (VD: Phòng 101 đã có chưa)
    db_room = room_crud.get_room_by_number(db, room_number=room.Room_Number)
    if db_room:
        raise HTTPException(status_code=400, detail="Room number already exists")
    
    return room_crud.create_room(db=db, room=room)

# 3. Xem chi tiết phòng
@router.get("/{room_id}", response_model=RoomResponse)
def read_room(room_id: int, db: Session = Depends(get_db)):
    db_room = room_crud.get_room(db, room_id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

# 4. Cập nhật phòng (Giá, Trạng thái...)
@router.put("/{room_id}", response_model=RoomResponse)
def update_room_info(room_id: int, room_in: RoomUpdate, db: Session = Depends(get_db)):
    db_room = room_crud.update_room(db, room_id, room_in)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

# 5. Xóa phòng
@router.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_room_api(room_id: int, db: Session = Depends(get_db)):
    db_room = room_crud.delete_room(db, room_id)
    if not db_room:
        raise HTTPException(status_code=404, detail="Room not found")
    return None