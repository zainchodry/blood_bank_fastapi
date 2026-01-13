from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.inventory import BloodInventory
from app.utils.jwt_handler import get_current_user

router = APIRouter(prefix="/inventory", tags=["Inventory"])


@router.get("/")
def view_inventory(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user.role not in ["admin", "staff"]:
        raise HTTPException(status_code=403, detail="Forbidden")

    return db.query(BloodInventory).all()
