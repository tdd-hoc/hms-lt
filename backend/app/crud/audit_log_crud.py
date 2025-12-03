from sqlalchemy.orm import Session
from typing import Optional
from app.models.audit_log import AuditLog
from app.schemas.audit_log_schema import AuditLogCreate

# 1. Lấy danh sách nhật ký (Hỗ trợ lọc theo Người dùng hoặc Nhân viên)
def get_audit_logs(
    db: Session, 
    skip: int = 0, 
    limit: int = 100, 
    staff_id: Optional[int] = None, 
    customer_id: Optional[int] = None
):
    query = db.query(AuditLog)
    
    if staff_id:
        query = query.filter(AuditLog.Staff_ID == staff_id)
    if customer_id:
        query = query.filter(AuditLog.Customer_ID == customer_id)
        
    # Sắp xếp mới nhất lên đầu
    return query.order_by(AuditLog.Timestamp.desc()).offset(skip).limit(limit).all()

# 2. Ghi nhật ký mới
def create_audit_log(db: Session, log: AuditLogCreate):
    # Lưu ý: Details là kiểu Dict (JSON), SQLAlchemy sẽ tự xử lý việc lưu vào cột JSON
    db_log = AuditLog(
        Staff_ID=log.Staff_ID,
        Customer_ID=log.Customer_ID,
        Action=log.Action,
        Details=log.Details
    )
    
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log