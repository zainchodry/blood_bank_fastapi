from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import BloodDonation, BloodGroup
from app.schemas.donation import DonationCreate
from app.utils.jwt_handler import get_current_user, role_required

router = APIRouter(prefix="/donations", tags=["Donations"])


@router.post("/")
def create_donation(
    data: DonationCreate,
    db: Session = Depends(get_db),
    user = Depends(role_required("donor"))
):
    if user.role != "donor":
        raise HTTPException(status_code=403, detail="Only donors can donate")

    bg = db.query(BloodGroup).filter(BloodGroup.name == data.blood_group_name).first()
    if not bg:
        raise HTTPException(status_code=400, detail="Invalid blood group")

    donation = BloodDonation(
        donor_id=user.id,
        blood_group_id=bg.id,
        units=data.units
    )
    db.add(donation)
    db.commit()
    return {"message": "Donation submitted"}


@router.get("/")
def list_donations(
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user.role in ["admin", "staff", "doctor"]:
        return db.query(BloodDonation).all()

    return db.query(BloodDonation).filter(BloodDonation.donor_id == user.id).all()
