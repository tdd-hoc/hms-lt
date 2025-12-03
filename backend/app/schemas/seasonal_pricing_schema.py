from pydantic import BaseModel, ConfigDict
from typing import Optional
from decimal import Decimal
from datetime import date
from app.models.seasonal_pricing import SeasonType # Import Enum

# 1. Base Schema
class SeasonalPricingBase(BaseModel):
    Room_Type: str
    Season_Type: SeasonType
    Price_Adjustment: Decimal
    Is_Multiplier: bool = False # False: Cộng tiền, True: Nhân hệ số
    Start_Date: Optional[date] = None
    End_Date: Optional[date] = None
    Description: Optional[str] = None

# 2. Create Schema
class SeasonalPricingCreate(SeasonalPricingBase):
    pass

# 3. Update Schema
class SeasonalPricingUpdate(BaseModel):
    Room_Type: Optional[str] = None
    Season_Type: Optional[SeasonType] = None
    Price_Adjustment: Optional[Decimal] = None
    Is_Multiplier: Optional[bool] = None
    Start_Date: Optional[date] = None
    End_Date: Optional[date] = None

# 4. Response Schema
class SeasonalPricingResponse(SeasonalPricingBase):
    Pricing_ID: int

    model_config = ConfigDict(from_attributes=True)