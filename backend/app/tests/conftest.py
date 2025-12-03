import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app.main import app
from app.config.database import Base, get_db

# 1. Cấu hình DB giả (SQLite) cho Test
# check_same_thread=False cần thiết cho SQLite khi chạy test
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 2. Fixture tạo DB: Chạy trước mỗi bài test
@pytest.fixture(scope="module")
def test_db():
    # Tạo bảng
    Base.metadata.create_all(bind=engine)
    yield # Chạy test ở đây
    # Xóa bảng sau khi test xong
    Base.metadata.drop_all(bind=engine)

# 3. Override dependency get_db của FastAPI
# Để ép App dùng DB test thay vì DB thật
def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# 4. Tạo TestClient
@pytest.fixture(scope="module")
def client(test_db):
    with TestClient(app) as c:
        yield c