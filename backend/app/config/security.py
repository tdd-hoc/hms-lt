from datetime import datetime, timedelta, timezone
from typing import Optional, Union, Any
from jose import jwt
from passlib.context import CryptContext
from .settings import settings

# Cấu hình context cho việc mã hóa mật khẩu sử dụng thuật toán bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Kiểm tra mật khẩu người dùng nhập vào có khớp với mật khẩu đã mã hóa trong DB không.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Mã hóa mật khẩu trước khi lưu vào Database.
    """
    return pwd_context.hash(password)

def create_access_token(subject: Union[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """
    Tạo ra chuỗi JWT Access Token.
    
    Args:
        subject: Thông tin chính để định danh (thường là User ID hoặc Email).
        expires_delta: Thời gian hết hạn tùy chỉnh (nếu có).
    """
    # 1. Lấy thời gian hiện tại
    expire = datetime.now(timezone.utc)
    
    # 2. Tính toán thời gian hết hạn
    if expires_delta:
        expire += expires_delta
    else:
        # Mặc định lấy từ settings (30 phút)
        expire += timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # 3. Tạo payload (dữ liệu chứa trong token)
    # 'sub' (Subject) là claim chuẩn của JWT để chứa định danh người dùng
    to_encode = {"exp": expire, "sub": str(subject)}
    
    # 4. Mã hóa payload thành chuỗi JWT
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    
    return encoded_jwt