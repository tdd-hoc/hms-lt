from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Any
from datetime import date, datetime
from decimal import Decimal
from app.models.booking import BookingStatus

# 1. Base Schema
class BookingBase(BaseModel):
    Checkin_Date: date
    Checkout_Date: date
    Status: Optional[BookingStatus] = BookingStatus.Reserved
    
    # JSON field lưu chi tiết cách tính giá (giảm giá, phụ phí...)
    Calculated_Price_Details: Optional[Any] = None 

# 2. Create Schema (Dữ liệu Frontend gửi lên khi đặt phòng)
class BookingCreate(BookingBase):
    Room_ID: int
    Customer_ID: Optional[int] = None # Có thể Null nếu Lễ tân tạo mà chưa gán khách
    
    # Lưu ý: Total_Amount thường được tính toán ở Backend chứ không tin tưởng số từ Frontend gửi lên
    # Nhưng nếu muốn cho phép override giá thủ công thì có thể thêm vào đây.

# 3. Update Schema (Dùng khi Check-in/Check-out hoặc Hủy)
class BookingUpdate(BaseModel):
    Checkin_Date: Optional[date] = None
    Checkout_Date: Optional[date] = None
    Status: Optional[BookingStatus] = None
    Total_Amount: Optional[Decimal] = None # Cập nhật lại tổng tiền nếu có phát sinh

# 4. Response Schema (Trả về cho Client)
class BookingResponse(BookingBase):
    Booking_ID: int
    Room_ID: int
    Customer_ID: Optional[int]
    Total_Amount: Optional[Decimal]
    Created_By_Staff_ID: Optional[int]
    
    Created_At: datetime
    Updated_At: Optional[datetime]

    # Dùng model_config thay vì class Config
    model_config = ConfigDict(from_attributes=True)