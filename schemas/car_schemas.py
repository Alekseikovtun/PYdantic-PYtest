from pydantic import BaseModel


class CarOnlyID(BaseModel):
    id: int

    class Config:
        orm_mode = True


class FullCar(CarOnlyID):
    color: str
    model: str
    gsb: str
