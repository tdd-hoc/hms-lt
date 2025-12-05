import os
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # --- Cấu hình App ---
    PROJECT_NAME: str = "Hotel Management System"
    API_V1_STR: str = "/api/v1"
    
    # ===> THÊM DÒNG NÀY ĐỂ SỬA LỖI ATTRIBUTE ERROR <===
    DEBUG: bool = True 
    
    # --- Cấu hình Database (Nhận từ .env) ---
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    # --- Cấu hình Bảo mật (JWT) ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8", 
        extra="ignore"
    )

    @property
    def SQLALCHEMY_DATABASE_URL(self) -> str:
        return f"mysql+mysqlconnector://{quote_plus(self.DB_USER)}:{quote_plus(self.DB_PASSWORD)}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()