from sqlalchemy import Column, Integer, String
from app.database import Base


class BloodGroup(Base):
    __tablename__ = "blood_groups"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    def __str__(self):
        return self.name
