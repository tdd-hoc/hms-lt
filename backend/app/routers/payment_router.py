from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.crud import payment_crud, booking_crud
from app.schemas.payment_schema import PaymentCreate, PaymentUpdate, PaymentResponse

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)

# 1. Ghi nhận thanh toán mới (Khách trả tiền)
@router.post("/", response_model=PaymentResponse, status_code=status.HTTP_201_CREATED)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    # Kiểm tra Booking tồn tại
    booking = booking_crud.get_booking(db, booking_id=payment.Booking_ID)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    return payment_crud.create_payment(db=db, payment=payment)

# 2. Lấy danh sách thanh toán (Admin xem doanh thu)
@router.get("/", response_model=List[PaymentResponse])
def read_payments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return payment_crud.get_all_payments(db, skip=skip, limit=limit)

# 3. Lấy lịch sử thanh toán của một Booking
@router.get("/booking/{booking_id}", response_model=List[PaymentResponse])
def read_payments_by_booking(booking_id: int, db: Session = Depends(get_db)):
    # Kiểm tra Booking tồn tại
    booking = booking_crud.get_booking(db, booking_id=booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
        
    return payment_crud.get_payments_by_booking(db, booking_id=booking_id)

# 4. Cập nhật thanh toán (Sửa lỗi hoặc cập nhật trạng thái từ Pending -> Paid)
@router.put("/{payment_id}", response_model=PaymentResponse)
def update_payment_info(payment_id: int, payment_in: PaymentUpdate, db: Session = Depends(get_db)):
    db_payment = payment_crud.update_payment(db, payment_id, payment_in)
    if not db_payment:
        raise HTTPException(status_code=404, detail="Payment transaction not found")
    return db_payment