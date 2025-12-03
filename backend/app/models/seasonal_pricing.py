import enum
from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, Date, Enum
from ..config.database import Base

class SeasonType(str, enum.Enum):
    Peak = "Peak"       # Mùa cao điểm
    OffPeak = "OffPeak" # Mùa thấp điểm
    Weekend = "Weekend" # Cuối tuần
    Holiday = "Holiday" # Ngày lễ
    Custom = "Custom"   # Tùy chỉnh khác

class SeasonalPricing(Base):
    __tablename__ = "Seasonal_Pricing"

    Pricing_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    # Loại phòng áp dụng (VD: "Deluxe", "Standard")
    # Lưu ý: Ở đây lưu String thay vì FK tới Room để áp dụng cho cả nhóm phòng
    Room_Type = Column(String(50), nullable=False)
    
    Season_Type = Column(Enum(SeasonType), nullable=False)
    
    # Giá trị điều chỉnh (VD: 500000 hoặc 1.5)
    Price_Adjustment = Column(DECIMAL(12, 2), nullable=False)
    
    # Cờ đánh dấu: 
    # True = Nhân (Base_Price * 1.5)
    # False = Cộng/Trừ (Base_Price + 500000)
    Is_Multiplier = Column(Boolean, default=False, nullable=False)
    
    Start_Date = Column(Date, nullable=True)
    End_Date = Column(Date, nullable=True)
    
    Description = Column(String(255), nullable=True)