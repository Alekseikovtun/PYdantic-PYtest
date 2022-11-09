from entry import app
from fastapi.testclient import TestClient


def test_1():
    with TestClient(app=app) as client:
        id: int = 1
        color: str = "brown"
        model: str = "BMW"
        gsb: str = "auto"
        json_data = {"id": id, "color": color, "model": model, "gsb": gsb}
        response = client.post(
            'http://127.0.0.1:8080/station/new_car1?',
            headers={"accept": "application/json"},
            json=json_data)
        assert response.status_code == 200


# def test_add_new_car_1():
#     id: int = 1
#     color: str = 'brown'
#     model: str = 'BMW'
#     gsb: str = 'auto'
#     json_data = {'id': id, 'color': color, 'model': model, 'gsb': gsb}
#     response = client.post('/station/new_car1', json=json_data) #, response_model=CarOnlyID
#     assert response.status_code == 200
