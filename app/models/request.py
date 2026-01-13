from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from app.database import Base


class BloodRequest(Base):
    __tablename__ = "blood_requests"

    id = Column(Integer, primary_key=True)
    requester_id = Column(Integer, ForeignKey("users.id"))
    blood_group_id = Column(Integer, ForeignKey("blood_groups.id"))
    units = Column(Integer)
    reason = Column(String)
    status = Column(String, default="pending")
    doctor_comment = Column(String, nullable=True)

    requester = relationship("User")
    blood_group = relationship("BloodGroup")
