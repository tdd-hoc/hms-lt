from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.payment import Payment, PaymentStatus
from app.schemas.payment_schema import PaymentCreate, PaymentUpdate

# 1. Lấy thông tin thanh toán theo ID
def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.Payment_ID == payment_id).first()

# 2. Lấy danh sách thanh toán của một Booking cụ thể
# Hàm này rất quan trọng để tính tổng tiền khách đã trả (Deposited + Paid)
def get_payments_by_booking(db: Session, booking_id: int):
    return db.query(Payment).filter(Payment.Booking_ID == booking_id).all()

# 3. Lấy tất cả thanh toán (Dùng cho báo cáo doanh thu Admin)
def get_all_payments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Payment).offset(skip).limit(limit).all()

# 4. Tạo giao dịch thanh toán mới
def create_payment(db: Session, payment: PaymentCreate):
    db_payment = Payment(
        Booking_ID=payment.Booking_ID,
        Invoice_ID=payment.Invoice_ID, # Có thể Null (nếu cọc trước khi xuất hóa đơn)
        Method=payment.Method,
        Amount=payment.Amount,
        Transaction_ID=payment.Transaction_ID,
        Status=payment.Status
    )
    
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# 5. Cập nhật giao dịch (Ví dụ: Từ Pending -> Paid, hoặc cập nhật Transaction_ID)
def update_payment(db: Session, payment_id: int, payment_update: PaymentUpdate):
    db_payment = get_payment(db, payment_id)
    if not db_payment:
        return None
    
    update_data = payment_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_payment, key, value)
        
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment