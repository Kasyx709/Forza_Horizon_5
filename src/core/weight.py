def modified_weight_class(_weight_class, race_type):
    if race_type == "rally":
        if _weight_class > 2:
            _weight_class = _weight_class - 2
        elif _weight_class == 2:
            _weight_class = _weight_class - 1
    elif race_type =="track":
        _weight_class = _weight_class + 1 if _weight_class < 4 else 4
    elif race_type in {"dirt", "snow"}:
        if 2 <= _weight_class <= 3:
            _weight_class = _weight_class - 1
        elif _weight_class == 4:
            _weight_class = _weight_class - 2
    return _weight_class

def vehicle_weight_class(vehicle_weight):
    if 3000 >= vehicle_weight:
        _weight_class = 1
    elif 3001 <= vehicle_weight <= 4000:
        _weight_class = 2
    elif 4001 <= vehicle_weight <= 5600:
        _weight_class = 3
    elif 5601 <= vehicle_weight:
        _weight_class = 4
    else:
        _weight_class = None
    return _weight_class


def weight_distribution(vehicle_weight, weight_percent_front):
    front_weight = vehicle_weight * weight_percent_front
    rear_weight = vehicle_weight - front_weight
    return front_weight, rear_weight
