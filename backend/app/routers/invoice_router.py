from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.crud import invoice_crud, booking_crud
from app.schemas.invoice_schema import InvoiceCreate, InvoiceUpdate, InvoiceResponse

router = APIRouter(
    prefix="/invoices",
    tags=["Invoices"]
)

# 1. Tạo hóa đơn mới
@router.post("/", response_model=InvoiceResponse, status_code=status.HTTP_201_CREATED)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    # Kiểm tra Booking có tồn tại không
    booking = booking_crud.get_booking(db, booking_id=invoice.Booking_ID)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    
    # Kiểm tra xem Booking này đã có hóa đơn chưa (Quan hệ 1-1)
    existing_invoice = invoice_crud.get_invoice_by_booking(db, booking_id=invoice.Booking_ID)
    if existing_invoice:
        raise HTTPException(status_code=400, detail="Invoice for this booking already exists")
        
    return invoice_crud.create_invoice(db=db, invoice=invoice)

# 2. Lấy hóa đơn theo ID
@router.get("/{invoice_id}", response_model=InvoiceResponse)
def read_invoice(invoice_id: int, db: Session = Depends(get_db)):
    db_invoice = invoice_crud.get_invoice(db, invoice_id=invoice_id)
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice

# 3. Lấy hóa đơn theo Booking ID (Tiện ích)
@router.get("/booking/{booking_id}", response_model=InvoiceResponse)
def read_invoice_by_booking(booking_id: int, db: Session = Depends(get_db)):
    db_invoice = invoice_crud.get_invoice_by_booking(db, booking_id=booking_id)
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found for this booking")
    return db_invoice

# 4. Cập nhật hóa đơn (Ví dụ: Chuyển trạng thái sang Paid)
@router.put("/{invoice_id}", response_model=InvoiceResponse)
def update_invoice_info(invoice_id: int, invoice_in: InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = invoice_crud.update_invoice(db, invoice_id, invoice_in)
    if not db_invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return db_invoice