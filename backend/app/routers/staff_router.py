from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from app.config.database import get_db
from app.config import security
from app.crud import staff_crud
from app.schemas.staff_schema import StaffCreate, StaffUpdate, StaffResponse
from app.schemas.token_schema import Token # Bạn cần tạo file này (xem bên dưới)

router = APIRouter(
    prefix="/staffs",
    tags=["Staffs"]
)

# 1. API Đăng nhập cho Nhân viên (Trả về JWT Token)
@router.post("/login", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Tìm nhân viên theo Email (form_data.username sẽ chứa email)
    staff = staff_crud.get_staff_by_email(db, email=form_data.username)
    
    # Kiểm tra: Không tìm thấy HOẶC Sai mật khẩu
    if not staff or not security.verify_password(form_data.password, staff.Password_Hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Kiểm tra: Tài khoản bị khóa
    if not staff.Is_Active:
        raise HTTPException(status_code=400, detail="Inactive user")

    # Tạo Token
    access_token = security.create_access_token(subject=staff.Staff_ID)
    return {"access_token": access_token, "token_type": "bearer"}

# 2. API Tạo nhân viên mới (Thường dành cho Admin)
@router.post("/", response_model=StaffResponse, status_code=status.HTTP_201_CREATED)
def create_new_staff(staff: StaffCreate, db: Session = Depends(get_db)):
    # Kiểm tra email trùng lặp
    db_staff = staff_crud.get_staff_by_email(db, email=staff.Email)
    if db_staff:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return staff_crud.create_staff(db=db, staff=staff)

# 3. API Lấy danh sách nhân viên
@router.get("/", response_model=List[StaffResponse])
def read_staffs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return staff_crud.get_all_staffs(db, skip=skip, limit=limit)

# 4. API Lấy chi tiết nhân viên theo ID
@router.get("/{staff_id}", response_model=StaffResponse)
def read_staff(staff_id: int, db: Session = Depends(get_db)):
    db_staff = staff_crud.get_staff(db, staff_id=staff_id)
    if db_staff is None:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff

# 5. API Cập nhật nhân viên
@router.put("/{staff_id}", response_model=StaffResponse)
def update_staff_info(staff_id: int, staff_in: StaffUpdate, db: Session = Depends(get_db)):
    db_staff = staff_crud.update_staff(db, staff_id, staff_in)
    if not db_staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return db_staff