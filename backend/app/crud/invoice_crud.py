from sqlalchemy.orm import Session
from app.models.invoice import Invoice, InvoiceStatus
from app.schemas.invoice_schema import InvoiceCreate, InvoiceUpdate

# 1. Lấy hóa đơn theo ID
def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.Invoice_ID == invoice_id).first()

# 2. Lấy hóa đơn theo Booking ID (Quan hệ 1-1)
# Giúp kiểm tra xem Booking này đã xuất hóa đơn hay chưa
def get_invoice_by_booking(db: Session, booking_id: int):
    return db.query(Invoice).filter(Invoice.Booking_ID == booking_id).first()

# 3. Tạo hóa đơn mới
def create_invoice(db: Session, invoice: InvoiceCreate):
    # Lưu ý: Các con số (Price, Tax, Total...) thường được tính toán 
    # ở tầng Service trước khi đẩy vào đây để lưu trữ.
    
    db_invoice = Invoice(
        Booking_ID=invoice.Booking_ID,
        Price=invoice.Price,
        Charges_Total=invoice.Charges_Total,
        Discount_Total=invoice.Discount_Total,
        Tax=invoice.Tax,
        Total=invoice.Total,
        Date=invoice.Date,
        Due_Date=invoice.Due_Date,
        Status=invoice.Status
    )
    
    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

# 4. Cập nhật hóa đơn (Thường là cập nhật Trạng thái thanh toán: Unpaid -> Paid)
def update_invoice(db: Session, invoice_id: int, invoice_update: InvoiceUpdate):
    db_invoice = get_invoice(db, invoice_id)
    if not db_invoice:
        return None
    
    update_data = invoice_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_invoice, key, value)

    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice