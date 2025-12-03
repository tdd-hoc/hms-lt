from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from decimal import Decimal
from app.models.room import RoomStatus # Import Enum từ Model

# 1. Base Schema
class RoomBase(BaseModel):
    Room_Number: str
    Room_Type: str
    Base_Price: Decimal # Sử dụng Decimal cho tiền tệ
    Status: Optional[RoomStatus] = RoomStatus.Available
    Amenities: Optional[str] = None
    
    # Pydantic sẽ tự động convert List Python thành JSON khi lưu DB
    Image_URLs: Optional[List[str]] = [] 

# 2. Create Schema
class RoomCreate(RoomBase):
    pass # Giống hệt Base, bắt buộc phải có các trường trên

# 3. Update Schema
class RoomUpdate(BaseModel):
    Room_Number: Optional[str] = None
    Room_Type: Optional[str] = None
    Base_Price: Optional[Decimal] = None
    Status: Optional[RoomStatus] = None
    Amenities: Optional[str] = None
    Image_URLs: Optional[List[str]] = None

# 4. Response Schema
class RoomResponse(RoomBase):
    Room_ID: int
    
    model_config = ConfigDict(from_attributes=True)