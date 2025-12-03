from typing import Optional
from sqlalchemy.orm import Session
from app.models.room import Room, RoomStatus
from app.schemas.room_schema import RoomCreate, RoomUpdate

# 1. Lấy thông tin phòng theo ID
def get_room(db: Session, room_id: int):
    return db.query(Room).filter(Room.Room_ID == room_id).first()

# 2. Lấy thông tin phòng theo Số phòng (Để kiểm tra trùng lặp)
def get_room_by_number(db: Session, room_number: str):
    return db.query(Room).filter(Room.Room_Number == room_number).first()

# 3. Lấy danh sách phòng (Có hỗ trợ lọc theo trạng thái)
# Ví dụ: get_rooms(db, status="Available") -> Chỉ trả về phòng trống
def get_rooms(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    status: Optional[RoomStatus] = None
):
    query = db.query(Room)
    
    if status:
        query = query.filter(Room.Status == status)
        
    return query.offset(skip).limit(limit).all()

# 4. Tạo phòng mới
def create_room(db: Session, room: RoomCreate):
    # Pydantic schema (List[str]) sẽ tự động được SQLAlchemy chuyển thành JSON cho MySQL
    db_room = Room(
        Room_Number=room.Room_Number,
        Room_Type=room.Room_Type,
        Base_Price=room.Base_Price,
        Status=room.Status,
        Amenities=room.Amenities,
        Image_URLs=room.Image_URLs # Truyền trực tiếp list vào
    )
    
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 5. Cập nhật thông tin phòng
def update_room(db: Session, room_id: int, room_update: RoomUpdate):
    db_room = get_room(db, room_id)
    if not db_room:
        return None
    
    update_data = room_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_room, key, value)

    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

# 6. Xóa phòng
def delete_room(db: Session, room_id: int):
    db_room = get_room(db, room_id)
    if db_room:
        db.delete(db_room)
        db.commit()
    return db_room