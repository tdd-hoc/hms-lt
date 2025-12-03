from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.crud import seasonal_pricing_crud
from app.schemas.seasonal_pricing_schema import SeasonalPricingCreate, SeasonalPricingUpdate, SeasonalPricingResponse

router = APIRouter(prefix="/seasonal-pricing", tags=["Seasonal Pricing"])

@router.get("/", response_model=List[SeasonalPricingResponse])
def read_pricing_rules(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return seasonal_pricing_crud.get_pricing_rules(db, skip, limit)

@router.post("/", response_model=SeasonalPricingResponse, status_code=status.HTTP_201_CREATED)
def create_pricing_rule(rule: SeasonalPricingCreate, db: Session = Depends(get_db)):
    return seasonal_pricing_crud.create_pricing_rule(db, rule)

@router.put("/{pricing_id}", response_model=SeasonalPricingResponse)
def update_pricing_rule(pricing_id: int, rule_in: SeasonalPricingUpdate, db: Session = Depends(get_db)):
    db_rule = seasonal_pricing_crud.update_pricing_rule(db, pricing_id, rule_in)
    if not db_rule:
        raise HTTPException(status_code=404, detail="Pricing rule not found")
    return db_rule

@router.delete("/{pricing_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_pricing_rule(pricing_id: int, db: Session = Depends(get_db)):
    db_rule = seasonal_pricing_crud.delete_pricing_rule(db, pricing_id)
    if not db_rule:
        raise HTTPException(status_code=404, detail="Pricing rule not found")
    return None