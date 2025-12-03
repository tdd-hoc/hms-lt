import enum
from sqlalchemy import Column, Integer, String, DECIMAL, Text, Enum
from ..config.database import Base

class AttractionType(str, enum.Enum):
    Airport = "Airport"
    TrainStation = "TrainStation"
    BusStation = "BusStation"
    CityCenter = "CityCenter"
    TouristSpot = "TouristSpot"

class NearbyAttraction(Base):
    __tablename__ = "Nearby_Attraction"

    Attraction_ID = Column(Integer, primary_key=True, index=True, autoincrement=True)
    
    Name_VI = Column(String(100), nullable=False) # Tên tiếng Việt
    Name_EN = Column(String(100), nullable=False) # Tên tiếng Anh
    
    # Khoảng cách (VD: 12.50 km)
    Distance_KM = Column(DECIMAL(5, 2), nullable=True)
    
    Type = Column(Enum(AttractionType), nullable=True)
    
    Description = Column(Text, nullable=True)