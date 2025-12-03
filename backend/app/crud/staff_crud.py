from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff_schema import StaffCreate, StaffUpdate
from app.config.security import get_password_hash

# 1. Lấy thông tin nhân viên theo ID
def get_staff(db: Session, staff_id: int):
    return db.query(Staff).filter(Staff.Staff_ID == staff_id).first()

# 2. Lấy thông tin nhân viên theo Email (Quan trọng cho việc Đăng nhập)
def get_staff_by_email(db: Session, email: str):
    return db.query(Staff).filter(Staff.Email == email).first()

# 3. Lấy danh sách toàn bộ nhân viên (Dành cho Admin xem)
def get_all_staffs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Staff).offset(skip).limit(limit).all()

# 4. Tạo nhân viên mới (Thường do Admin tạo)
def create_staff(db: Session, staff: StaffCreate):
    # Bước 1: Mã hóa mật khẩu
    hashed_password = get_password_hash(staff.Password)
    
    # Bước 2: Tạo đối tượng Model
    db_staff = Staff(
        Name=staff.Name,
        Role=staff.Role, # Role: Admin, Receptionist, hoặc Housekeeping
        Email=staff.Email,
        Phone_Number=staff.Phone_Number,
        Password_Hash=hashed_password,
        Is_Active=staff.Is_Active # Mặc định là True
    )
    
    # Bước 3: Lưu vào DB
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

# 5. Cập nhật thông tin nhân viên
def update_staff(db: Session, staff_id: int, staff_update: StaffUpdate):
    db_staff = get_staff(db, staff_id)
    if not db_staff:
        return None
    
    # Lấy dữ liệu cần update (bỏ qua các trường None)
    update_data = staff_update.model_dump(exclude_unset=True)
    
    for key, value in update_data.items():
        setattr(db_staff, key, value)
    
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

# 6. Xóa nhân viên (Hoặc khóa tài khoản)
# Lưu ý: Thay vì xóa cứng (Delete), ta thường dùng update_staff để set Is_Active = False
def delete_staff(db: Session, staff_id: int):
    db_staff = get_staff(db, staff_id)
    if db_staff:
        db.delete(db_staff)
        db.commit()
    return db_staff