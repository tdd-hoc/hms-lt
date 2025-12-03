from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import date
from app.models.invoice import InvoiceStatus # Import Enum

# 1. Base Schema
class InvoiceBase(BaseModel):
    Price: Decimal          # Tiền phòng
    Charges_Total: Decimal  # Tổng phụ phí
    Discount_Total: Decimal # Tổng giảm giá
    Tax: Decimal            # Thuế
    Total: Decimal          # Tổng cộng thanh toán
    
    Date: date              # Ngày xuất hóa đơn
    Due_Date: Optional[date] = None # Hạn thanh toán
    Status: Optional[InvoiceStatus] = InvoiceStatus.Unpaid

# 2. Create Schema (Thường dùng nội bộ hoặc Admin tạo thủ công)
class InvoiceCreate(InvoiceBase):
    Booking_ID: int # Hóa đơn bắt buộc phải gắn với 1 Booking

# 3. Update Schema (Cập nhật trạng thái thanh toán)
class InvoiceUpdate(BaseModel):
    Status: Optional[InvoiceStatus] = None
    Due_Date: Optional[date] = None

# 4. Response Schema
class InvoiceResponse(InvoiceBase):
    Invoice_ID: int
    Booking_ID: int

    model_config = ConfigDict(from_attributes=True)