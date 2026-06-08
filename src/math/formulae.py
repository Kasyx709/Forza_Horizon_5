import math

gravity = 32.2  # expressed as ft/s^2
inches_per_second = gravity * 12
motion_ratio = 1
weight_to_mass = 32.174048556
lb_to_kg_conversion = 0.453592
nm_to_nmm_conversion = 0.001
nmm_to_lbin_conversion = 5.7101471627692

corner_mass = lambda _weight, _weight_percent: (_weight * _weight_percent / weight_to_mass) / 2
spring_formula = lambda _frequency, _corner_mass: round(0.5*
    (2 * math.pi * _frequency) ** 2 * _corner_mass / motion_ratio ** 2
    , 1)
