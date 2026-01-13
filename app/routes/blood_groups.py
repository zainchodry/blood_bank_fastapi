from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.blood_group import BloodGroup
from app.database import get_db

router = APIRouter(prefix="/blood-groups", tags=["Blood Groups"])


@router.get("/")
def get_blood_groups(db: Session = Depends(get_db)):
    return db.query(BloodGroup).all()
