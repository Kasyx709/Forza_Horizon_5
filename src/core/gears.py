import math
from typing import Dict

drivetrain_weight_offsets: Dict = {
    "RWD": 60
    , "AWD": 50
    , "FWD": 40
}

tire_coefficients: Dict = {
    "Standard": 1.0,
    "Street": 1.06,
    "Sport": 1.13,
    "Snow": 1.06,
    "Offroad": 1.09,
    "Rally": 1.16,
    "Drag": 0.95,
    "Drift": 1.15,
    "Semi-slick": 1.25,
    "Slick": 1.29,
    "Vintage": 1.0,
    "VintageRace": 1.0,
}

surface_coefficients: Dict = {
    "Dirt": 0.0,
    "Asphalt": 1,
}


def gear_ratio_calculator(
        vehicle_weight: int
        , vehicle_torque: int
        , drivetrain_type: str
        , rpm_redline: int
        , number_of_gears: int
        , tire_compound: str
        , tire_size: set
        , final_drive_ratio: float
) -> Dict[str, float]:
    """
    Returns gear ratio given rpm, tire diameter, and torque using the following formulas:

    Max Tire Speed at a given RPM:
        MPH,max = wheel RPM * Tire Circumference * 1/1056

    Maximum Tire Traction Force:
      Fmax = μ * W
        μ = friction coefficient (how sticky the tire is)
            Forze Horizon uses the following:
                Standard: 1.0
                Road Tires:
                    Street: 1.06
                    Sport: 1.13
                Offroad Tires:
                    Snow: 1.06
                    Offroad: 1.09
                    Rally: 1.16
                Race:
                    Semi-Slick: 1.25
                    Slick: 1.29
                Drag: 0.95
                Drift: 1.15
        W = Weight on the driven wheels (not total car weight), taken from a percentage of total weight
            60% for RWD

    r = tire radius (in feet)
    drivetrain type: RWD, AWD, FWD
    weight_shift_pct: assumed weight shift pct
    :param vehicle_torque: Expressed as a percentage of total torque
    :param drivetrain_type:
    :param vehicle_weight: Weight of the Vehicle
    :param rpm_redline: Maximum Rotations Per Minute (RPM) before the engine reaches redline
    :param number_of_gears: Total number of Gears within the transmission
    :param tire_size: Tire size, sidewall and overall diameter
    :param tire_compound: The type of tire compound used, relates to spinout calculations.
    :param final_drive_ratio: Transmission Ratio
    :return: Gear Ratio
    """
    # tire coefficient = 1.0 for street to 1.7 for race slicks
    # torque available at ~3500 rpm = 92% of maximum
    # tire pressure has some effect, unknown at this time. I suspect it effects contact points
    width, sidewall_height, wheel_diameter = tire_size
    number_of_mm_per_inch = 25.4
    inches_per_minute_to_miles_per_hour_conversion_ratio = 1 / 1056
    torque_coefficient = 0.915
    gear_coefficient = 0.87
    _next_gear = lambda x, y: round(x * gear_coefficient - y, 2)
    tire_size_in_inches = (width * sidewall_height / 100 / number_of_mm_per_inch) * 2 + 15
    tire_size_in_feet: float = (tire_size_in_inches * 0.5) / 12
    wheel_rpm = rpm_redline * 1 / (final_drive_ratio * 3.66)
    maximum_speed: int = math.floor(
        math.pi * tire_size_in_inches * wheel_rpm * inches_per_minute_to_miles_per_hour_conversion_ratio
    )
    weight_at_wheels: int = vehicle_weight * drivetrain_weight_offsets[drivetrain_type.upper()] / 100
    maximum_contact_force: float = weight_at_wheels * tire_coefficients[tire_compound] * tire_size_in_feet
    maximum_traction: float = maximum_contact_force / (final_drive_ratio * vehicle_torque * torque_coefficient)
    gear_ratios: Dict[str, float] = {
        "Final Drive Ratio": final_drive_ratio,
    }
    for surface_type in surface_coefficients:
        _max_safe_first = round(maximum_traction + surface_coefficients[surface_type], 2)
        _current_gear: float = _max_safe_first
        gear_ratios[surface_type] = [_max_safe_first]
        _gears: Dict = {}
        for _gear in range(2, number_of_gears + 1):
            __next_gear = _next_gear(_current_gear, 0 if _gear <= 3 else 0.1)
            _gears.update({f"Gear# {_gear}": __next_gear})
            _current_gear = __next_gear
        gear_ratios[surface_type] = gear_ratios[surface_type] + list(_gears.values())
    return gear_ratios


if __name__ == '__main__':
    gear = gear_ratio_calculator(2007, 426, "RWD", 11000, 6, "Slick", {380, 40, 15}, 4.10)
    print(gear.items())
