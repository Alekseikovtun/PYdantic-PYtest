from entry import app
from api.api import api_router
from fastapi.testclient import TestClient
from schemas.car_schemas import CarOnlyID, FullCar


client = TestClient(app)


def test_add_new_car_1():
    id: int = 1
    color: str = 'brown'
    model: str = 'BMW'
    gsb: str = 'auto'
    json_data = {'id': id, 'color': color, 'model': model, 'gsb': gsb}
    response = client.post('/station/new_car1/', json=json_data) #, response_model=CarOnlyID
    assert response.status_code == 200
