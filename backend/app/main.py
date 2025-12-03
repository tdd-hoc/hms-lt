 # Entry point (FastAPI app)


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import settings
from app.config.database import engine, Base
from app.routers import (staff_router, customer_router, room_router, booking_router, invoice_router, payment_router,
    staff_router, customer_router, room_router, booking_router,
    invoice_router, payment_router, 
    booking_charge_router, housekeeping_router, audit_log_router, 
    nearby_attraction_router, seasonal_pricing_router

)
# --- Quan Trọng: Import tất cả các Models ---
# Phải import models vào đây để SQLAlchemy nhận diện và tạo bảng
from app.models import (
    staff,
    customer,
    room,
    booking,
    invoice,
    payment,
    booking_charge,
    housekeeping,
    audit_log,
    nearby_attraction,
    seasonal_pricing
)

# 1. Tự động tạo bảng trong Database
# Lệnh này sẽ kiểm tra metadata của Base và tạo các bảng chưa tồn tại.
# Trong môi trường Production, nên dùng Alembic để migrate, nhưng ở đây dùng cách này cho nhanh.
Base.metadata.create_all(bind=engine)

# 2. Khởi tạo ứng dụng FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    debug=settings.DEBUG
)

# 3. Cấu hình CORS (Cross-Origin Resource Sharing)
# Cho phép Frontend (React/Vue/Angular) gọi API tới Backend
origins = [
    "http://localhost",
    "http://localhost:3000", # Port thường dùng của React
    "http://localhost:5173", # Port thường dùng của Vite/Vue
    "*"                      # Hoặc để "*" để cho phép tất cả (chỉ dùng khi dev)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Cho phép tất cả các method: GET, POST, PUT, DELETE...
    allow_headers=["*"],
)

# Các API sẽ có dạng: /api/v1/staffs/login, /api/v1/customers/register...
app.include_router(staff_router.router, prefix=settings.API_V1_STR)
app.include_router(customer_router.router, prefix=settings.API_V1_STR)
app.include_router(room_router.router, prefix=settings.API_V1_STR)
app.include_router(booking_router.router, prefix=settings.API_V1_STR)
app.include_router(invoice_router.router, prefix=settings.API_V1_STR)
app.include_router(payment_router.router, prefix=settings.API_V1_STR)
app.include_router(booking_charge_router.router, prefix=settings.API_V1_STR)
app.include_router(housekeeping_router.router, prefix=settings.API_V1_STR)
app.include_router(audit_log_router.router, prefix=settings.API_V1_STR)
app.include_router(nearby_attraction_router.router, prefix=settings.API_V1_STR)
app.include_router(seasonal_pricing_router.router, prefix=settings.API_V1_STR)

# 4. Route kiểm tra sức khỏe hệ thống (Health Check)
@app.get("/")
def read_root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME} API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    }

# --- Nơi đăng ký các Routers sau này ---
# Ví dụ: app.include_router(auth_router, prefix="/auth")