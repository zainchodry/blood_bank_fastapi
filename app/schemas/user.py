from pydantic import BaseModel, EmailStr
from app.utils.enums import UserRole

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: UserRole = UserRole.REQUESTER


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: UserRole

    class Config:
        orm_mode = True

class LoginCreate(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str = "bearer"

