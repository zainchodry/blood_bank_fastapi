from sqlalchemy import Column, Integer, String, Boolean, Enum
from app.database import Base
from app.utils.enums import UserRole

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.REQUESTER, nullable=False)
    is_active = Column(Boolean, default=True)

    def __str__(self):
        return f"{self.full_name} ({self.role})"
