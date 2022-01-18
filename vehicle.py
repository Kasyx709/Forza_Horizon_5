from suspension import calc_suspension

class Vehicle(object):
    def __init__(self, vehicle_name, vehicle_weight, front_height, rear_height, front_wt_pct, terrain_type):
        self.vehicle_name = vehicle_name
        self.vehicle_weight: int = vehicle_weight
        self.height_front: float = front_height
        self.height_rear: float = rear_height
        self.weight_percent_front: float = front_wt_pct * 0.01
        suspension_settings = calc_suspension(self, terrain_type)
        for k in suspension_settings.__dict__:
            if not k == 'vehicle':
                v = suspension_settings.__getattribute__(k)
                if isinstance(v, float):
                    v = round(v, 1)
                    self.__setattr__(k, v)

    def vehicle_attributes(self):
        for k in self.__dict__:
            print(k, self.__getattribute__(k))