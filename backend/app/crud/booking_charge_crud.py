from sqlalchemy.orm import Session
from app.models.booking_charge import BookingCharge
from app.schemas.booking_charge_schema import BookingChargeCreate, BookingChargeUpdate

# 1. Lấy chi tiết một khoản phí
def get_charge(db: Session, charge_id: int):
    return db.query(BookingCharge).filter(BookingCharge.Charge_ID == charge_id).first()

# 2. Lấy toàn bộ phụ phí của một Booking (Quan trọng để tính tổng tiền)
def get_charges_by_booking(db: Session, booking_id: int):
    return db.query(BookingCharge).filter(BookingCharge.Booking_ID == booking_id).all()

# 3. Tạo khoản phí mới
def create_charge(db: Session, charge: BookingChargeCreate):
    db_charge = BookingCharge(
        Booking_ID=charge.Booking_ID,
        Description=charge.Description,
        Amount=charge.Amount,
        Staff_Recorded_ID=charge.Staff_Recorded_ID
    )
    db.add(db_charge)
    db.commit()
    db.refresh(db_charge)
    return db_charge

# 4. Cập nhật khoản phí (Sửa tiền hoặc mô tả)
def update_charge(db: Session, charge_id: int, charge_update: BookingChargeUpdate):
    db_charge = get_charge(db, charge_id)
    if not db_charge:
        return None
    
    update_data = charge_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_charge, key, value)
        
    db.add(db_charge)
    db.commit()
    db.refresh(db_charge)
    return db_charge

# 5. Xóa khoản phí (Nếu nhập nhầm)
def delete_charge(db: Session, charge_id: int):
    db_charge = get_charge(db, charge_id)
    if db_charge:
        db.delete(db_charge)
        db.commit()
    return db_charge