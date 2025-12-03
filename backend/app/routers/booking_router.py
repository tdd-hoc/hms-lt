from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.crud import booking_crud, room_crud
from app.schemas.booking_schema import BookingCreate, BookingUpdate, BookingResponse
from app.models.booking import BookingStatus

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"]
)

# 1. Tạo Booking (Đặt phòng)
@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
def create_booking(booking: BookingCreate, db: Session = Depends(get_db)):
    # Bước 1: Kiểm tra xem Phòng có tồn tại không
    room = room_crud.get_room(db, room_id=booking.Room_ID)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")

    # Bước 2: Quan trọng - Kiểm tra trùng lịch
    is_available = booking_crud.check_room_availability(
        db, 
        room_id=booking.Room_ID, 
        checkin=booking.Checkin_Date, 
        checkout=booking.Checkout_Date
    )
    
    if not is_available:
        raise HTTPException(
            status_code=400, 
            detail="Room is already booked for the selected dates."
        )

    # Bước 3: Nếu hợp lệ thì tạo Booking
    # (Lưu ý: tham số staff_id có thể lấy từ Token nếu làm chức năng Lễ tân đặt hộ)
    return booking_crud.create_booking(db=db, booking=booking)

# 2. Lấy danh sách Booking (Lọc theo khách, phòng, trạng thái)
@router.get("/", response_model=List[BookingResponse])
def read_bookings(
    skip: int = 0, 
    limit: int = 100, 
    customer_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[BookingStatus] = None,
    db: Session = Depends(get_db)
):
    return booking_crud.get_bookings(
        db, 
        skip=skip, 
        limit=limit, 
        customer_id=customer_id, 
        room_id=room_id, 
        status=status
    )

# 3. Lấy chi tiết Booking
@router.get("/{booking_id}", response_model=BookingResponse)
def read_booking(booking_id: int, db: Session = Depends(get_db)):
    db_booking = booking_crud.get_booking(db, booking_id=booking_id)
    if db_booking is None:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking

# 4. Cập nhật Booking (Hủy phòng, Check-in, Check-out)
@router.put("/{booking_id}", response_model=BookingResponse)
def update_booking_info(booking_id: int, booking_in: BookingUpdate, db: Session = Depends(get_db)):
    db_booking = booking_crud.update_booking(db, booking_id, booking_in)
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return db_booking