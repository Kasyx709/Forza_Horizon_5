"""
Calculates suspension settings using 2.8875 constant
2.8875/([front+rear height]/2)=spring rate total/2 weight.

Using imperial units, multiply weight*dist*value from below,
ex. 2133lbs, 52% - 1066lbs over the front axle, 2133*0.52*0.2=221.8 front spring.
Multiply by 1-dist (1-0.52=0.48) for rear springs.

1.98hz - 0.20 - Soft
2.21hz - 0.25
2.42hz - 0.30 - Moderate
2.62hz - 0.35
2.80hz - 0.40 - Stiff
3.13hz - 0.50
3.43hz - 0.60 - Heavy aero/limited travel
3.70hz - 0.70
3.96hz - 0.80 - Heavy aero+limited travel

To balance the springs perfectly, sweep the rear spring +/- 0.5lb per 25
(ex. with 520 front 480 rear spring, try between 475 and 485 rear).
Still in imperial units, for a specific frequency as a measure of relative
stiffness, where mass represents the weight over the axle and K is spring rate in lb, use K=(Hz²M)/19.56.
To find the rates of an existing tune use Hz=(K/M*19.56)².
"""

spring_constant: float = 2.8875


class Suspension(object):
    rebound_max = 20
    bump_max = 20
    terrain_types = [
        "cross country",
        "dirt",
        "road",
        "snow",
    ]
    stiffness_range = {
        1: (0.20, 0.25),  # soft
        2: (0.30, 0.35),  # moderate
        3: (0.40, 0.50),  # stiff
        4: (0.6, 0.8),  # heavy
    }
    categories = {"Roll bar",
                  "Spring",
                  "Rebound",
                  "Bump",
                  "Differential"}

    def __init__(self, vehicle_name):
        self.vehicle_name = vehicle_name
        self.arb_front: float
        self.arb_rear: float
        self.spring_front: float
        self.spring_rear: float
        self.rebound_front: float
        self.rebound_rear: float
        self.bump_front: float
        self.bump_rear: float
        super().__init__()

    def damper_settings(self, spring_front, spring_rear, total_weight):
        front_rebound = self.rebound_max * (spring_front / total_weight)
        rear_rebound = self.rebound_max * (spring_rear / total_weight)
        front_bump = front_rebound * 0.5
        rear_bump = rear_rebound * 0.7
        return front_rebound, rear_rebound, front_bump, rear_bump

    def stiffness(self, total_weight, terrain_type):
        assert terrain_type in self.terrain_types
        weight_class = vehicle_weight_class(total_weight)
        if terrain_type == "cross country":
            if weight_class > 2:
                weight_class = weight_class - 2
            elif weight_class == 2:
                weight_class = weight_class - 1
        elif terrain_type in {"dirt", "snow"}:
            if 2 <= weight_class < 3:
                weight_class = weight_class - 1
            elif weight_class == 4:
                weight_class = weight_class - 2
        stiffness = self.stiffness_range[weight_class]
        return stiffness


def vehicle_weight_class(total_weight):
    weight_class = None
    if 3000 >= total_weight:
        weight_class = 1
    elif 3001 <= total_weight <= 4000:
        weight_class = 2
    elif 4001 <= total_weight <= 5600:
        weight_class = 3
    elif 5601 <= total_weight:
        weight_class = 4
    return weight_class


def weight_distribution(vehicle_weight, weight_percent_front):
    front_weight = vehicle_weight * weight_percent_front
    rear_weight = vehicle_weight - front_weight
    return front_weight, rear_weight


def spring_settings(stiffness_rating, vehicle_weight, weight_percent_front, height, is_rear: bool = False):
    weight_percent = weight_percent_front
    if is_rear:
        weight_percent = 1 - weight_percent_front
        stiffness_rating = stiffness_rating[1]
    else:
        stiffness_rating = stiffness_rating[0]
    # spring_stiffness = lambda h: (stiffness_rating / h) / 2
    spring_rate = (vehicle_weight * weight_percent) * stiffness_rating
    return spring_rate


def arb_settings(total_weight, spring_rate, is_rear: bool = False):
    arb_value = (65 / spring_rate) * 68
    return arb_value * 1.2 if is_rear else arb_value # 20% increase in rear sway for enhanced cornering


def diff_settings(weight_percent_front, spring_multi):
    diff_setting = (100 / weight_percent_front) * spring_multi
    return diff_setting if diff_setting <= 100 else 100


def calc_suspension(vehicle, terrain_type):
    vehicle_name = vehicle.vehicle_name
    vehicle_weight = vehicle.vehicle_weight
    suspension = Suspension(vehicle_name)
    stiffness = suspension.stiffness(vehicle_weight, terrain_type)

    spring_front, spring_rear = \
        suspension.spring_front, suspension.spring_rear = \
        spring_settings(stiffness, vehicle_weight, vehicle.weight_percent_front, vehicle.height_front), \
        spring_settings(stiffness, vehicle_weight, (1 - vehicle.weight_percent_front), vehicle.height_rear,
                        is_rear=True)
    suspension.rebound_front, suspension.rebound_rear, suspension.bump_front, suspension.bump_rear = \
        suspension.damper_settings(spring_front, spring_rear, vehicle_weight)
    suspension.arb_front = arb_settings(vehicle_weight, suspension.spring_front)
    suspension.arb_rear = arb_settings(vehicle_weight, suspension.spring_rear,
                                       is_rear=True)
    # diff_settings = _diff_settings(spring_multi),
    # items = [round(x, 1) for i in [arb_settings, spring_settings, damper_settings] for x in i]
    # suspension_values = *map(lambda c, v: {c: v}, categories, items),
    return suspension


if __name__ == '__main__':
    pass
