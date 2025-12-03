from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.crud import nearby_attraction_crud
from app.schemas.nearby_attraction_schema import AttractionCreate, AttractionUpdate, AttractionResponse

router = APIRouter(prefix="/attractions", tags=["Nearby Attractions"])

@router.get("/", response_model=List[AttractionResponse])
def read_attractions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return nearby_attraction_crud.get_attractions(db, skip, limit)

@router.post("/", response_model=AttractionResponse, status_code=status.HTTP_201_CREATED)
def create_attraction(attraction: AttractionCreate, db: Session = Depends(get_db)):
    return nearby_attraction_crud.create_attraction(db, attraction)

@router.put("/{attraction_id}", response_model=AttractionResponse)
def update_attraction(attraction_id: int, attraction_in: AttractionUpdate, db: Session = Depends(get_db)):
    db_attr = nearby_attraction_crud.update_attraction(db, attraction_id, attraction_in)
    if not db_attr:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return db_attr

@router.delete("/{attraction_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_attraction(attraction_id: int, db: Session = Depends(get_db)):
    db_attr = nearby_attraction_crud.delete_attraction(db, attraction_id)
    if not db_attr:
        raise HTTPException(status_code=404, detail="Attraction not found")
    return None