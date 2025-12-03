from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import List

from app.config.database import get_db
from app.config import security
from app.crud import customer_crud
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate, CustomerResponse
from app.schemas.token_schema import Token

from fastapi import BackgroundTasks # <--- Import
from app.services.email_service import email_service


router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)

# 1. Đăng ký khách hàng mới (Đã tích hợp gửi mail)
@router.post("/register", response_model=CustomerResponse, status_code=status.HTTP_201_CREATED)
def register_customer(
    customer: CustomerCreate, 
    background_tasks: BackgroundTasks, # <--- Khai báo tham số này
    db: Session = Depends(get_db)
):
    # Kiểm tra email tồn tại
    db_customer = customer_crud.get_customer_by_email(db, email=customer.Email)
    if db_customer:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Tạo user trong DB
    new_customer = customer_crud.create_customer(db=db, customer=customer)
    
    # === GỌI SERVICE GỬI MAIL (CHẠY NGẦM) ===
    # Hàm này sẽ in log ra terminal giả lập việc gửi mail
    email_service.send_welcome_email(
        background_tasks, 
        email_to=new_customer.Email, 
        name=new_customer.Name
    )
    
    return new_customer

# 2. Đăng nhập khách hàng (Lấy Token)
@router.post("/login", response_model=Token)
def login_customer(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Tìm khách hàng
    customer = customer_crud.get_customer_by_email(db, email=form_data.username)
    
    # Verify mật khẩu
    if not customer or not security.verify_password(form_data.password, customer.Password_Hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Tạo Token (Subject là Customer_ID)
    access_token = security.create_access_token(subject=customer.Customer_ID)
    return {"access_token": access_token, "token_type": "bearer"}

# 3. Lấy danh sách khách hàng (Thường cho Admin/Lễ tân)
@router.get("/", response_model=List[CustomerResponse])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return customer_crud.get_customers(db, skip=skip, limit=limit)

# 4. Lấy chi tiết khách hàng
@router.get("/{customer_id}", response_model=CustomerResponse)
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = customer_crud.get_customer(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

# 5. Cập nhật hồ sơ khách hàng
@router.put("/{customer_id}", response_model=CustomerResponse)
def update_customer_profile(customer_id: int, customer_in: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = customer_crud.update_customer(db, customer_id, customer_in)
    if not db_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer