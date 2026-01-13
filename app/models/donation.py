from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class BloodDonation(Base):
    __tablename__ = "blood_donations"

    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey("users.id"))
    blood_group_id = Column(Integer, ForeignKey("blood_groups.id"))
    units = Column(Integer)
    status = Column(String, default="pending")
    staff_comment = Column(String, nullable=True)

    donor = relationship("User")
    blood_group = relationship("BloodGroup")
