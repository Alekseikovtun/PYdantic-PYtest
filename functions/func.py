from models.car import Car


def add_car(id, color, model, gsb):
    new_car = Car(id, color, model, gsb)
    return new_car
