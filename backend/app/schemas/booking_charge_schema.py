from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import datetime

# 1. Base Schema
class BookingChargeBase(BaseModel):
    Description: str
    Amount: Decimal

# 2. Create Schema
class BookingChargeCreate(BookingChargeBase):
    Booking_ID: int
    Staff_Recorded_ID: Optional[int] = None # Có thể null nếu hệ thống tự động tính

# 3. Update Schema (Ví dụ: Nhập sai tiền cần sửa lại)
class BookingChargeUpdate(BaseModel):
    Description: Optional[str] = None
    Amount: Optional[Decimal] = None

# 4. Response Schema
class BookingChargeResponse(BookingChargeBase):
    Charge_ID: int
    Booking_ID: int
    Staff_Recorded_ID: Optional[int]
    Charge_Date: datetime

    # Dùng model_config thay vì class Config
    model_config = ConfigDict(from_attributes=True)