from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from app.models.nearby_attraction import AttractionType # Import Enum

# 1. Base Schema
class AttractionBase(BaseModel):
    Name_VI: str
    Name_EN: str
    Distance_KM: Optional[Decimal] = None
    Type: Optional[AttractionType] = None
    Description: Optional[str] = None

# 2. Create Schema
class AttractionCreate(AttractionBase):
    pass

# 3. Update Schema
class AttractionUpdate(BaseModel):
    Name_VI: Optional[str] = None
    Name_EN: Optional[str] = None
    Distance_KM: Optional[Decimal] = None
    Type: Optional[AttractionType] = None
    Description: Optional[str] = None

# 4. Response Schema
class AttractionResponse(AttractionBase):
    Attraction_ID: int

    model_config = ConfigDict(from_attributes=True)