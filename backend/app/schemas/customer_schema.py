from pydantic import BaseModel, EmailStr,ConfigDict
from typing import Optional
from datetime import datetime

# 1. Base Schema: Chứa các trường chung
class CustomerBase(BaseModel):
    Name: str
    Surname: Optional[str] = None
    Phone_Number: Optional[str] = None
    Address: Optional[str] = None
    Age: Optional[int] = None
    Postal_Code: Optional[str] = None
    Email: Optional[EmailStr] = None # EmailStr tự động validate định dạng a@b.com
    Gender: Optional[str] = None

# 2. Create Schema: Dùng khi User đăng ký (Cần Password)
class CustomerCreate(CustomerBase):
    Password: str  # Password nhập vào (plain text)
    Email: EmailStr # Khi đăng ký bắt buộc phải có Email

# 3. Update Schema: Dùng khi User cập nhật hồ sơ (Tất cả đều Optional)
class CustomerUpdate(BaseModel):
    Name: Optional[str] = None
    Surname: Optional[str] = None
    Phone_Number: Optional[str] = None
    Address: Optional[str] = None
    Email: Optional[EmailStr] = None

# 4. Response Schema: Dùng để trả dữ liệu về Frontend (Không có Password)
class CustomerResponse(CustomerBase):
    Customer_ID: int
    Created_At: datetime

    model_config = ConfigDict(from_attributes=True)