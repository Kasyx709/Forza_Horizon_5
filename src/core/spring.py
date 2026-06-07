from math import pi

spring_constant: float = 2.8875


def spring_rate(stiffness_rating, vehicle_weight,
                weight_distribution_pct,
                spring_multiplier: float,
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

    :param spring_multiplier: Multiplies spring rate values to account for various spring types
    :param stiffness_rating: the range of natural frequency values to consider
    :param vehicle_weight: Assumed as lbs and converted to kg
    :param weight_distribution_pct: percentage of vehicles weight over axle
    :param is_rear: boolean, denotes whether value is for front/rear spring
    :param frequency_offset_pct: This is the difference between front and rear ride frequencies.
    Front values are typically 10-20% higher than rear.
    :return: Values for spring rate in lbs/in
    """
    lb_to_kg_conversion = 0.453592
    nm_to_nmm_conversion = 0.001
    nmm_to_lbin_conversion = 5.7101471627692
    frequency_offset_pct = 1.175
    motion_ratio = 1
    weight_percent = weight_distribution_pct * .01
    stiffness = stiffness_rating[0]
    if is_rear:
        weight_percent = 1 - weight_percent
        if stiffness * frequency_offset_pct >= stiffness_rating[1]:
            stiffness = stiffness_rating[1]
        else:
            stiffness = stiffness * frequency_offset_pct
    axle_weight_kg = (vehicle_weight * lb_to_kg_conversion * weight_percent)
    spring_formula = 4 * pi ** 2 * stiffness ** 2 * axle_weight_kg / motion_ratio ** 2
    spring_rate_lb_in = spring_formula * nm_to_nmm_conversion * nmm_to_lbin_conversion
    return spring_rate_lb_in * spring_multiplier


def track_spring_rate(vehicle_weight: int, spring_rate_lb_in: float):
    if vehicle_weight <= 3000:
        spring_rate_lb_in = spring_rate_lb_in * 1.4
    elif 3000 < vehicle_weight <= 3500:
        spring_rate_lb_in = spring_rate_lb_in * 0.55
    elif 3500 < vehicle_weight:
        spring_rate_lb_in = spring_rate_lb_in * .3
    return spring_rate_lb_in