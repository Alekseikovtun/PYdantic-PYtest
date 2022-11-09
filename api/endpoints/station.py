from fastapi import APIRouter
from functions.func import add_car
from schemas.car_schemas import CarOnlyID, FullCar


router = APIRouter()


@router.post('/new_car1', response_model=CarOnlyID)
def add_new_car1(
    id: int,
    color: str,
    model: str,
    gsb: str
) -> CarOnlyID:
    new_car = add_car(id, color, model, gsb)
    result = CarOnlyID.from_orm(new_car)
    return result


@router.post('/new_car2', response_model=FullCar)
def add_new_car2(
    id: int,
    color: str,
    model: str,
    gsb: str
) -> FullCar:
    new_car = add_car(id, color, model, gsb)
    result = FullCar.from_orm(new_car)
    return result
