from sqlalchemy.orm import Session
from app.models.nearby_attraction import NearbyAttraction
from app.schemas.nearby_attraction_schema import AttractionCreate, AttractionUpdate

# 1. Lấy chi tiết địa điểm
def get_attraction(db: Session, attraction_id: int):
    return db.query(NearbyAttraction).filter(NearbyAttraction.Attraction_ID == attraction_id).first()

# 2. Lấy danh sách địa điểm
def get_attractions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(NearbyAttraction).offset(skip).limit(limit).all()

# 3. Tạo địa điểm mới
def create_attraction(db: Session, attraction: AttractionCreate):
    db_attraction = NearbyAttraction(
        Name_VI=attraction.Name_VI,
        Name_EN=attraction.Name_EN,
        Distance_KM=attraction.Distance_KM,
        Type=attraction.Type,
        Description=attraction.Description
    )
    db.add(db_attraction)
    db.commit()
    db.refresh(db_attraction)
    return db_attraction

# 4. Cập nhật địa điểm
def update_attraction(db: Session, attraction_id: int, attraction_update: AttractionUpdate):
    db_attraction = get_attraction(db, attraction_id)
    if not db_attraction:
        return None
    
    update_data = attraction_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_attraction, key, value)

    db.add(db_attraction)
    db.commit()
    db.refresh(db_attraction)
    return db_attraction

# 5. Xóa địa điểm
def delete_attraction(db: Session, attraction_id: int):
    db_attraction = get_attraction(db, attraction_id)
    if db_attraction:
        db.delete(db_attraction)
        db.commit()
    return db_attraction