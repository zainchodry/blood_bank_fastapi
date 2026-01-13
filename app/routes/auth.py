from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models.user import *
from app.schemas.user import *
from app.database import *
from app.utils.jwt_handler import *

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register", response_model=UserOut)
def register(user:UserCreate, db:Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email Already Exists")
    if user.role not in ["admin", "doctor", "staff", "donor", "requester"]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Role")
    
    new_user = User(
        full_name = user.full_name,
        email = user.email,
        password = hash_password(user.password),
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/login", response_model=Token)
def login(user: LoginCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Email Or Password"
        )

    token = access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
