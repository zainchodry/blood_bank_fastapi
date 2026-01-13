from pydantic import BaseModel


class BloodGroupOut(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
