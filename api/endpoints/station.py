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
    result = CarOnlyID.schema(new_car)
    return result
    # return new_car


@router.post('/new_car2', response_model=FullCar)
def add_new_car2(
    id: int,
    color: str,
    model: str,
    gsb: str
) -> FullCar:
    new_car = add_car(id, color, model, gsb)
    result = FullCar(new_car)
    return result
    # return new_car
