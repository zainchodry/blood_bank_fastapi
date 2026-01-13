from pydantic import BaseModel


class RequestCreate(BaseModel):
    blood_group_name: str
    units: int
    reason: str


class RequestOut(BaseModel):
    id: int
    requester: str
    blood_group: str
    units: int
    status: str
    doctor_comment: str | None

    class Config:
        orm_mode = True
