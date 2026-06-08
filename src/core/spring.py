from src.math.formulae import spring_formula, axle_mass, vehicle_mass, frequency_offset

spring_constant: float = 2.8875


def _base_frequency(_weight: int, frequencies: tuple):
    _frequency = frequencies[0] + (1000 * frequencies[1] - _weight) / 100
    if _frequency < frequencies[0]:
        _frequency = frequencies[0]
    elif _frequency > frequencies[1]:
        _frequency = frequencies[1]
    return _frequency


def spring_rate(natural_frequency, vehicle_weight,
                weight_distribution_pct,
                ):
    """
    Calculates Spring Rate using natural frequency values
    K = (4π²F²M)/mr²
    F = NATURAL FREQUENCY (HZ)
       F = 1/(2π)√(K/M)
    K = SPRING RATE (N/M)
    M = MASS (KG)
    MR = MOTION RATIO (Forza does not simulate MR so MR = 1)

    0.5-1.0Hz Passenger cars, typical OEM
    1.0-1.5Hz Typical lowering springs
    1.5-2.0Hz Rally Cars
    1.5-2.5Hz Non-Aero racecars, moderate downforce Formula cars
    2.5-3.5Hz Moderate downforce racecars with up to 50% total weight in max downforce capability
    3.5-5.0+Hz High downforce racecars with more than 50% of their weight in max downforce

    :param natural_frequency: the range of natural frequency values to consider
    :param vehicle_weight: Assumed as lbs and converted to kg
    :param weight_distribution_pct: percentage of vehicles weight over axle
    :return: Values for spring rate in lbs/in
    """
    # If weight increases by X%, natural frequency drops by roughly X/2%
    # lighter side gets the higher natural frequency
    _minimum_frequency_offset = 1.175
    frequency_max = _base_frequency(vehicle_weight, natural_frequency)
    _front_bias = weight_distribution_pct * 0.01
    _vehicle_mass = vehicle_mass(vehicle_weight)
    _front_axle_, _rear_axle = axle_mass(_vehicle_mass, _front_bias)
    _the_front_weighs_more = False
    if _front_axle_ > _rear_axle:
        _the_front_weighs_more = True
        _frequency_offset = frequency_offset(_front_axle_, _rear_axle)
    else:
        _frequency_offset = frequency_offset(_rear_axle, _front_axle_)
    if _frequency_offset < _minimum_frequency_offset:
        _frequency_offset = _minimum_frequency_offset
    frequency_min = round(frequency_max / _frequency_offset, 2)
    if _the_front_weighs_more:
        _softer_spring = spring_formula(frequency_min, _front_axle_)
        _stiffer_spring = spring_formula(frequency_max, _rear_axle)
    else:
        _softer_spring = spring_formula(frequency_min, _rear_axle)
        _stiffer_spring = spring_formula(frequency_max, _front_axle_)
    return _softer_spring, _stiffer_spring


def track_spring_rate(vehicle_weight: int, spring_rate_lb_in: float):
    if vehicle_weight <= 3000:
        spring_rate_lb_in = spring_rate_lb_in * 1.4
    elif 3000 < vehicle_weight <= 3500:
        spring_rate_lb_in = spring_rate_lb_in * 0.55
    elif 3500 < vehicle_weight:
        spring_rate_lb_in = spring_rate_lb_in * .3
    return spring_rate_lb_in
