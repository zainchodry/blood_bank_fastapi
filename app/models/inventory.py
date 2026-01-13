from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class BloodInventory(Base):
    __tablename__ = "blood_inventory"

    id = Column(Integer, primary_key=True)
    blood_group_id = Column(Integer, ForeignKey("blood_groups.id"))
    available_units = Column(Integer, default=0)

    blood_group = relationship("BloodGroup")
