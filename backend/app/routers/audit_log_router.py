from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.config.database import get_db
from app.crud import audit_log_crud
from app.schemas.audit_log_schema import AuditLogCreate, AuditLogResponse

router = APIRouter(prefix="/audit-logs", tags=["Audit Logs"])

# 1. Xem nhật ký (Lọc theo user gây ra hành động)
@router.get("/", response_model=List[AuditLogResponse])
def read_logs(
    skip: int = 0, 
    limit: int = 100, 
    staff_id: Optional[int] = None,
    customer_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    return audit_log_crud.get_audit_logs(db, skip, limit, staff_id, customer_id)

# 2. Ghi nhật ký thủ công (Thường ít dùng, vì hệ thống tự log)
@router.post("/", response_model=AuditLogResponse)
def create_log(log: AuditLogCreate, db: Session = Depends(get_db)):
    return audit_log_crud.create_audit_log(db, log)