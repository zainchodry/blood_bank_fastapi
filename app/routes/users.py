from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.utils.jwt_handler import *

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(role_required("admin"))
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden")
    return db.query(User).all()
