from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.crud import booking_charge_crud, booking_crud
from app.schemas.booking_charge_schema import BookingChargeCreate, BookingChargeUpdate, BookingChargeResponse

router = APIRouter(prefix="/booking-charges", tags=["Booking Charges"])

# 1. Thêm khoản phí vào Booking
@router.post("/", response_model=BookingChargeResponse, status_code=status.HTTP_201_CREATED)
def create_charge(charge: BookingChargeCreate, db: Session = Depends(get_db)):
    booking = booking_crud.get_booking(db, booking_id=charge.Booking_ID)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking_charge_crud.create_charge(db, charge)

# 2. Xem danh sách phí của một Booking
@router.get("/booking/{booking_id}", response_model=List[BookingChargeResponse])
def read_charges_by_booking(booking_id: int, db: Session = Depends(get_db)):
    booking = booking_crud.get_booking(db, booking_id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking_charge_crud.get_charges_by_booking(db, booking_id)

# 3. Cập nhật khoản phí
@router.put("/{charge_id}", response_model=BookingChargeResponse)
def update_charge(charge_id: int, charge_in: BookingChargeUpdate, db: Session = Depends(get_db)):
    db_charge = booking_charge_crud.update_charge(db, charge_id, charge_in)
    if not db_charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    return db_charge

# 4. Xóa khoản phí
@router.delete("/{charge_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_charge(charge_id: int, db: Session = Depends(get_db)):
    db_charge = booking_charge_crud.delete_charge(db, charge_id)
    if not db_charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    return None