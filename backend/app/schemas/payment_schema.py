from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import datetime
from app.models.payment import PaymentMethod, PaymentStatus # Import Enum

# 1. Base Schema
class PaymentBase(BaseModel):
    Booking_ID: int
    Method: PaymentMethod # Ví dụ: Cash, Momo, Visa...
    Amount: Decimal
    Transaction_ID: Optional[str] = None # Mã giao dịch từ ngân hàng/ví điện tử
    Status: Optional[PaymentStatus] = PaymentStatus.Paid

# 2. Create Schema (Dữ liệu gửi lên khi thanh toán)
class PaymentCreate(PaymentBase):
    Invoice_ID: Optional[int] = None # Có thể thanh toán cọc trước khi có hóa đơn

# 3. Update Schema (Thường dùng để cập nhật trạng thái nếu thanh toán async)
class PaymentUpdate(BaseModel):
    Status: Optional[PaymentStatus] = None
    Transaction_ID: Optional[str] = None
    Invoice_ID: Optional[int] = None

# 4. Response Schema
class PaymentResponse(PaymentBase):
    Payment_ID: int
    Invoice_ID: Optional[int]
    Payment_Date: datetime

    model_config = ConfigDict(from_attributes=True)