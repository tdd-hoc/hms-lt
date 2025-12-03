from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.staff import StaffRole # Import Enum từ Model

# 1. Base Schema
class StaffBase(BaseModel):
    Name: str
    Role: StaffRole # Validate chỉ nhận: Admin, Receptionist, Housekeeping
    Email: EmailStr
    Phone_Number: Optional[str] = None
    Is_Active: Optional[bool] = True

# 2. Create Schema (Cần Password)
class StaffCreate(StaffBase):
    Password: str

# 3. Update Schema (Chỉ Admin mới update Role, nhưng ở đây ta cứ define chung)
class StaffUpdate(BaseModel):
    Name: Optional[str] = None
    Phone_Number: Optional[str] = None
    Is_Active: Optional[bool] = None
    # Lưu ý: Không cho update Password ở đây (nên làm API đổi pass riêng)

# 4. Response Schema (Trả về Client)
class StaffResponse(StaffBase):
    Staff_ID: int
    Created_At: datetime

    model_config = ConfigDict(from_attributes=True)