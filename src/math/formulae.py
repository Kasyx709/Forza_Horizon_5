import math

gravity = 32.2  # expressed as ft/s^2
inches_per_second = gravity * 12
motion_ratio = 0.98
weight_to_mass = 32.174048556
lb_to_kg_conversion = 0.453592
nm_to_lbin = 0.00571
nm_to_nmm_conversion = 0.001
nmm_to_lbin_conversion = 5.7101471627692

vehicle_mass = lambda _vehicle_weight: _vehicle_weight * lb_to_kg_conversion
axle_mass = lambda _vehicle_mass, _front_bias: (
    round(_vehicle_mass * _front_bias, 2),
    round(_vehicle_mass * (1 - _front_bias), 2)
)
frequency_offset = lambda _heavier_weight, _lighter_weight: round((_heavier_weight / _lighter_weight), 2)


def spring_formula(_frequency, _axle_mass):
    _spring_rate = (4 * math.pi ** 2) * (_frequency ** 2) * (_axle_mass / 2) / motion_ratio ** 2
    _spring_rate_lb_in = _spring_rate * nm_to_lbin
    return _spring_rate_lb_in
