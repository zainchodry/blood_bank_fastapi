from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import BloodRequest, BloodGroup
from app.schemas.request import RequestCreate
from app.utils.jwt_handler import get_current_user, role_required

router = APIRouter(prefix="/requests", tags=["Blood Requests"])


@router.post("/")
def create_request(
    data: RequestCreate,
    db: Session = Depends(get_db),
    user = Depends(role_required("requester"))
):
    if user.role != "requester":
        raise HTTPException(status_code=403, detail="Only requesters allowed")

    bg = db.query(BloodGroup).filter(BloodGroup.name == data.blood_group_name).first()
    if not bg:
        raise HTTPException(status_code=400, detail="Invalid blood group")

    req = BloodRequest(
        requester_id=user.id,
        blood_group_id=bg.id,
        units=data.units,
        reason=data.reason
    )
    db.add(req)
    db.commit()
    return {"message": "Request submitted"}


@router.patch("/{request_id}/decision")
def approve_or_reject_request(
    request_id: int,
    status: str,
    comment: str,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    if user.role not in ["doctor", "admin"]:
        raise HTTPException(status_code=403, detail="Permission denied")

    req = db.query(BloodRequest).get(request_id)
    req.status = status
    req.doctor_comment = comment
    db.commit()
    return {"message": "Request updated"}
