from pydantic import BaseModel


class CarOnlyID(BaseModel):
    id: int


class FullCar(CarOnlyID):
    color: str
    model: str
    gsb: str
