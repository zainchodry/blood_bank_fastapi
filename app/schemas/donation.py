from pydantic import BaseModel


class DonationCreate(BaseModel):
    blood_group_name: str
    units: int


class DonationOut(BaseModel):
    id: int
    donor: str
    blood_group: str
    units: int
    status: str

    class Config:
        orm_mode = True
