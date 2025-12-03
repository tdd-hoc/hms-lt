from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
from datetime import datetime

# 1. Base Schema
class AuditLogBase(BaseModel):
    Action: str
    Details: Optional[Dict[str, Any]] = None # Dữ liệu JSON linh hoạt

# 2. Create Schema (Thường hệ thống tự tạo, không public ra API ngoài)
class AuditLogCreate(AuditLogBase):
    Staff_ID: Optional[int] = None
    Customer_ID: Optional[int] = None

# 3. Response Schema
class AuditLogResponse(AuditLogBase):
    Log_ID: int
    Staff_ID: Optional[int]
    Customer_ID: Optional[int]
    Timestamp: datetime

    model_config = ConfigDict(from_attributes=True)