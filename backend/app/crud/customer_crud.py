from sqlalchemy.orm import Session
from app.models.customer import Customer
from app.schemas.customer_schema import CustomerCreate, CustomerUpdate
from app.config.security import get_password_hash

# 1. Lấy thông tin khách hàng bằng ID
def get_customer(db: Session, customer_id: int):
    return db.query(Customer).filter(Customer.Customer_ID == customer_id).first()

# 2. Lấy thông tin khách hàng bằng Email (Dùng cho Login)
def get_customer_by_email(db: Session, email: str):
    return db.query(Customer).filter(Customer.Email == email).first()

# 3. Lấy danh sách khách hàng (Phân trang)
def get_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Customer).offset(skip).limit(limit).all()

# 4. Tạo khách hàng mới (Register)
def create_customer(db: Session, customer: CustomerCreate):
    # Bước quan trọng: Băm mật khẩu trước khi lưu
    hashed_password = get_password_hash(customer.Password)
    
    # Tạo đối tượng Model từ dữ liệu Schema
    # Lưu ý: Chúng ta map thủ công hoặc dùng dict unpack để thay Password bằng Password_Hash
    db_customer = Customer(
        Name=customer.Name,
        Surname=customer.Surname,
        Phone_Number=customer.Phone_Number,
        Address=customer.Address,
        Age=customer.Age,
        Postal_Code=customer.Postal_Code,
        Email=customer.Email,
        Gender=customer.Gender,
        Password_Hash=hashed_password # Lưu chuỗi đã mã hóa
    )
    
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer) # Refresh để lấy lại ID và Created_At từ DB
    return db_customer

# 5. Cập nhật thông tin khách hàng
def update_customer(db: Session, customer_id: int, customer_update: CustomerUpdate):
    # Tìm khách hàng trong DB
    db_customer = get_customer(db, customer_id)
    if not db_customer:
        return None
    
    # Chuyển dữ liệu update thành dictionary, loại bỏ các giá trị None
    update_data = customer_update.model_dump(exclude_unset=True)
    
    # Cập nhật các trường
    for key, value in update_data.items():
        setattr(db_customer, key, value)

    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

# 6. Xóa khách hàng (Optional - Thường ít dùng, chỉ Admin mới được xóa)
def delete_customer(db: Session, customer_id: int):
    db_customer = get_customer(db, customer_id)
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer