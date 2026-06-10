from typing import Dict, Optional

drivetrain_weight_offsets: Dict = {
    "RWD": 0.60
    , "AWD": 0.5
    , "FWD": 0.40
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
    "Semislick": 1.25,
    "Slick": 1.29,
    "Vintage": 1.0,
    "VintageRace": 1.0,
}

# 77
surface_coefficients: Dict = {
    "Asphalt": 0.9,  # Teste Values
    "Dirt": 0.7,
}


def gear_ratio_calculator(
        vehicle_weight: int
        , vehicle_torque: int
        , drivetrain_type: str
        , rpm_redline: int
        , number_of_gears: int
        , tire_compound: str
        , tire_size: set
        , turbo_psi: Optional[float] = None
) -> dict[str, dict[str, float]]:
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
    Atmospheric pressure ≈ 14.7 psi. (used for boost calculations)
    :param turbo_psi:
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
    atmospheric_pressure = 14.7
    turbo_efficiency_coefficient = 0.8
    tire_size_in_inches = (width * sidewall_height / 100 / number_of_mm_per_inch) * 2 + 15
    tire_size_in_feet: float = (tire_size_in_inches * 0.5) / 12
    weight_at_wheels: int = vehicle_weight * drivetrain_weight_offsets[drivetrain_type.upper()]
    if turbo_psi and turbo_psi > 0:
        _boost_multiplier = round(
            (turbo_psi + atmospheric_pressure) * turbo_efficiency_coefficient * 1 / atmospheric_pressure, 2)
        vehicle_torque = vehicle_torque * _boost_multiplier
    _maximum_contact_force: float = weight_at_wheels * tire_coefficients[tire_compound] * tire_size_in_feet
    gear_ratios: Dict[str, Dict[str, float]] = {}
    for surface_type in surface_coefficients:
        gear_ratios[surface_type] = _gear_ratios(
            surface_type, vehicle_torque, tire_size_in_inches,
            _maximum_contact_force, number_of_gears, rpm_redline
        )
    return gear_ratios

def _gear_ratios(
        surface_type: str
        , _torque
        , tire_size_in_inches
        , maximum_contact_force
        , number_of_gears
        , rpm_redline
) -> Dict[str, float]:
    _gear_coefficient = 0.8
    _torque_coefficient = 0.875
    _gears: Dict = {i: 0.0 for i in range(1, number_of_gears + 1)}
    _next_gear = lambda x, y: round(x * _gear_coefficient - y, 2)
    _final_drive_ratio = 6.10
    _peak_power = rpm_redline * 0.9
    while next(reversed(_gears.values())) < 0.76:
        _max_traction: float = maximum_contact_force / (_final_drive_ratio * _torque * _torque_coefficient)
        _first_gear: float = round(_max_traction + surface_coefficients[surface_type], 2)
        _gears[1] = _first_gear
        wheel_rpm = round(rpm_redline / (_final_drive_ratio * _first_gear), 0)
        _engine_rpm = round(wheel_rpm * _final_drive_ratio * _first_gear, 0)
        # maximum_speed: int = math.floor(math.pi * tire_size_in_inches * wheel_rpm * inches_per_minute_to_miles_per_hour_conversion_ratio)
        if _engine_rpm > rpm_redline:
            _final_drive_ratio = _final_drive_ratio - 0.01 if _final_drive_ratio > 2.2 else 2.2
            continue
        else:
            _current_gear = _gears[1]
            for _gear_number in range(2, number_of_gears + 1):
                _gear = _next_gear(_current_gear, 0 if _gear_number <= (number_of_gears - 2) else 0.01)
                _gears.update({_gear_number: _gear})
                _current_gear = _gear
            if next(reversed(_gears.values())) < 0.76:
                _final_drive_ratio = _final_drive_ratio - 0.01 if _final_drive_ratio > 2.2 else 2.2
    _gears["Final Drive Ratio"] = round(_final_drive_ratio, 2)
    return _gears


if __name__ == '__main__':
    pass
