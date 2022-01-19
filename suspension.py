"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""

from math import pi

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
        1: (1.5, 2.0),  # Rally Cars
        2: (1.5, 2.5),  # Non-Aero racecars, moderate downforce Formula cars
        3: (2.5, 3.50),  # Moderate downforce racecars with up to 50% total weight in max downforce capability
        4: (3.5, 5.0),  # High downforce racecars with more than 50% of their weight in max downforce
    }
    categories = {"Roll bar",
                  "Spring",
                  "Rebound",
                  "Bump",
                  "Differential"}

    def __init__(self):
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
        front_bump = front_rebound * 0.65
        rear_bump = rear_rebound * 0.65
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


def spring_settings(stiffness_rating, vehicle_weight,
                    weight_percent_front,
                    is_rear: bool = False):
    """
    Calculates Spring Rate using natural frequency values
    K= (4π²F²M)/mr²
    F = NATURAL FREQUENCY (HZ)
    K = SPRING RATE (N/M)
    M = MASS (KG)
    MR = MOTION RATIO (Forza does not simulate MR so MR = 1)

    0.5-1.0Hz Passenger cars, typical OEM
    1.0-1.5Hz Typical lowering springs
    1.5-2.0Hz Rally Cars
    1.5-2.5Hz Non-Aero racecars, moderate downforce Formula cars
    2.5-3.5Hz Moderate downforce racecars with up to 50% total weight in max downforce capability
    3.5-5.0+Hz High downforce racecars with more than 50% of their weight in max downforce

    :param stiffness_rating:
    :param vehicle_weight: Assumed as lbs and converted to kg
    :param weight_percent_front: percentage of vehicles weight over axle
    :param is_rear: boolean, denotes whether value is for front/rear spring
    :return: spring values
    """
    lb_to_kg_conversion = 0.453592
    nm_to_nmm_conversion = 0.001
    nmm_to_lbin_conversion = 5.7101471627692
    frequency_offset_pct = 1.15
    motion_ratio = 1
    weight_percent = weight_percent_front
    stiffness = stiffness_rating[0]
    if is_rear:
        weight_percent = 1 - weight_percent_front
        if stiffness * frequency_offset_pct >= stiffness_rating[1]:
            stiffness = stiffness_rating[1]
        else:
            stiffness = stiffness * frequency_offset_pct
    axle_weight_kg = (vehicle_weight * lb_to_kg_conversion * weight_percent)
    spring_rate = (((4 * pi ** 2 * stiffness ** 2 * axle_weight_kg / motion_ratio ** 2) *
                    nm_to_nmm_conversion) * nmm_to_lbin_conversion)
    return spring_rate


def arb_settings(transmission, spring_rate, is_rear: bool = False):
    arb_value = (65 / spring_rate) * 68
    if is_rear:
        if transmission == "fwd":
            arb_value = arb_value * 1.25
        elif transmission == "rwd":
            arb_value = arb_value * 1.15
        elif transmission == "awd":
            arb_value = arb_value * 1.1
    return arb_value


def diff_settings(weight_percent_front, spring_multi):
    diff_setting = (100 / weight_percent_front) * spring_multi
    return diff_setting if diff_setting <= 100 else 100


def calc_suspension(vehicle, drivetrain, terrain_type):
    vehicle_type = vehicle.vehicle_type
    vehicle_weight = vehicle.vehicle_weight
    suspension = Suspension()
    stiffness = suspension.stiffness(vehicle_weight, terrain_type)
    spring_front, spring_rear = \
        suspension.spring_front, suspension.spring_rear = \
        spring_settings(stiffness, vehicle_weight, vehicle.weight_percent_front), \
        spring_settings(stiffness, vehicle_weight, vehicle.weight_percent_front, is_rear=True)
    suspension.rebound_front, suspension.rebound_rear, suspension.bump_front, suspension.bump_rear = \
        suspension.damper_settings(spring_front, spring_rear, vehicle_weight)
    suspension.arb_front = arb_settings(drivetrain, suspension.spring_front)
    suspension.arb_rear = arb_settings(drivetrain, suspension.spring_rear, is_rear=True)
    return suspension


if __name__ == '__main__':
    pass
