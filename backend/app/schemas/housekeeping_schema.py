
from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date
from app.models.housekeeping import HousekeepingStatus # Import Enum

# 1. Base Schema
class HousekeepingBase(BaseModel):
    Task_Date: date
    Notes: Optional[str] = None
    Status: Optional[HousekeepingStatus] = HousekeepingStatus.Pending

# 2. Create Schema
class HousekeepingCreate(HousekeepingBase):
    Room_ID: int
    Staff_ID: Optional[int] = None # Có thể chưa phân công ngay lúc tạo

# 3. Update Schema (Dùng cho nhân viên cập nhật trạng thái "Done")
class HousekeepingUpdate(BaseModel):
    Staff_ID: Optional[int] = None # Phân công nhân viên mới
    Status: Optional[HousekeepingStatus] = None
    Notes: Optional[str] = None

# 4. Response Schema
class HousekeepingResponse(HousekeepingBase):
    Task_ID: int
    Room_ID: int
    Staff_ID: Optional[int]

    model_config = ConfigDict(from_attributes=True)