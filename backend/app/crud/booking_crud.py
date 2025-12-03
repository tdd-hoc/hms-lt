from sqlalchemy.orm import Session
from sqlalchemy import and_
from datetime import date
from typing import Optional, List

from app.models.booking import Booking, BookingStatus
from app.schemas.booking_schema import BookingCreate, BookingUpdate

# 1. Hàm kiểm tra phòng trống (Logic cốt lõi)
def check_room_availability(db: Session, room_id: int, checkin: date, checkout: date):
    """
    Kiểm tra xem phòng có bị trùng lịch không.
    Trả về True nếu phòng trống, False nếu đã bị đặt.
    """
    # Logic trùng lịch:
    # (Ngày checkin mới < Ngày checkout cũ) VÀ (Ngày checkout mới > Ngày checkin cũ)
    # Và trạng thái booking cũ KHÔNG phải là Cancelled
    
    overlapping_booking = db.query(Booking).filter(
        Booking.Room_ID == room_id,
        Booking.Status.notin_([BookingStatus.Cancelled, BookingStatus.NoShow]),
        and_(
            Booking.Checkin_Date < checkout,
            Booking.Checkout_Date > checkin
        )
    ).first()
    
    if overlapping_booking:
        return False # Có trùng lịch -> Phòng không trống
    return True # Không trùng -> Phòng trống

# 2. Lấy thông tin Booking theo ID
def get_booking(db: Session, booking_id: int):
    return db.query(Booking).filter(Booking.Booking_ID == booking_id).first()

# 3. Lấy danh sách Booking (Hỗ trợ lọc đa dạng)
def get_bookings(
    db: Session, 
    skip: int = 0, 
    limit: int = 100,
    customer_id: Optional[int] = None,
    room_id: Optional[int] = None,
    status: Optional[BookingStatus] = None
):
    query = db.query(Booking)
    
    # Các bộ lọc tùy chọn
    if customer_id:
        query = query.filter(Booking.Customer_ID == customer_id)
    if room_id:
        query = query.filter(Booking.Room_ID == room_id)
    if status:
        query = query.filter(Booking.Status == status)
        
    return query.offset(skip).limit(limit).all()

# 4. Tạo Booking mới
def create_booking(db: Session, booking: BookingCreate, staff_id: Optional[int] = None):
    # Lưu ý: Việc gọi check_room_availability nên được thực hiện ở tầng Router
    # trước khi gọi hàm này để trả về lỗi 400 Bad Request rõ ràng hơn.
    
    db_booking = Booking(
        Customer_ID=booking.Customer_ID,
        Room_ID=booking.Room_ID,
        Checkin_Date=booking.Checkin_Date,
        Checkout_Date=booking.Checkout_Date,
        Status=booking.Status, # Mặc định là Reserved
        Calculated_Price_Details=booking.Calculated_Price_Details,
        Created_By_Staff_ID=staff_id # Nếu Lễ tân tạo thì lưu ID lễ tân
    )
    
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# 5. Cập nhật Booking (Check-in, Check-out, Hủy...)
def update_booking(db: Session, booking_id: int, booking_update: BookingUpdate):
    db_booking = get_booking(db, booking_id)
    if not db_booking:
        return None
    
    update_data = booking_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_booking, key, value)
        
    # Tự động cập nhật timestamp Updated_At (SQLAlchemy xử lý, nhưng gọi lại cho chắc)
    # db_booking.Updated_At = func.now() 

    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking

# 6. Xóa Booking (Thường rất ít dùng, thay vào đó là đổi Status="Cancelled")
def delete_booking(db: Session, booking_id: int):
    db_booking = get_booking(db, booking_id)
    if db_booking:
        db.delete(db_booking)
        db.commit()
    return db_booking