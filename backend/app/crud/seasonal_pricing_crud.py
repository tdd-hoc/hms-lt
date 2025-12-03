from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from datetime import date
from app.models.seasonal_pricing import SeasonalPricing
from app.schemas.seasonal_pricing_schema import SeasonalPricingCreate, SeasonalPricingUpdate

# 1. Lấy quy tắc giá theo ID
def get_pricing_rule(db: Session, pricing_id: int):
    return db.query(SeasonalPricing).filter(SeasonalPricing.Pricing_ID == pricing_id).first()

# 2. Lấy tất cả quy tắc
def get_pricing_rules(db: Session, skip: int = 0, limit: int = 100):
    return db.query(SeasonalPricing).offset(skip).limit(limit).all()

# 3. Tìm các quy tắc giá có hiệu lực cho một loại phòng trong khoảng thời gian cụ thể
# Hàm này cực kỳ quan trọng cho logic tính tiền tự động
def get_applicable_rules(db: Session, room_type: str, check_date: date):
    return db.query(SeasonalPricing).filter(
        SeasonalPricing.Room_Type == room_type,
        and_(
            SeasonalPricing.Start_Date <= check_date,
            SeasonalPricing.End_Date >= check_date
        )
    ).all()

# 4. Tạo quy tắc mới
def create_pricing_rule(db: Session, rule: SeasonalPricingCreate):
    db_rule = SeasonalPricing(
        Room_Type=rule.Room_Type,
        Season_Type=rule.Season_Type,
        Price_Adjustment=rule.Price_Adjustment,
        Is_Multiplier=rule.Is_Multiplier,
        Start_Date=rule.Start_Date,
        End_Date=rule.End_Date,
        Description=rule.Description
    )
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

# 5. Cập nhật quy tắc
def update_pricing_rule(db: Session, pricing_id: int, rule_update: SeasonalPricingUpdate):
    db_rule = get_pricing_rule(db, pricing_id)
    if not db_rule:
        return None
    
    update_data = rule_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_rule, key, value)

    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

# 6. Xóa quy tắc
def delete_pricing_rule(db: Session, pricing_id: int):
    db_rule = get_pricing_rule(db, pricing_id)
    if db_rule:
        db.delete(db_rule)
        db.commit()
    return db_rule