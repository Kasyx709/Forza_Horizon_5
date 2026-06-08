# Conversion from Weight -> mass = Weight / 32.2 | 32.5 = half of 65
_antirollbar_modifier: float = 32.5


def antiroll_bar(_front_spring: float, _rear_spring, front_bias):
    _front_spring_stiffness = (2 * _front_spring) * (72 / 2) ** 2
    _rear_spring_stiffness = (2 * _rear_spring) * (72 / 2) ** 2
    _front_bias = (front_bias / 100) + 0.05
    total_stiffness = _front_spring_stiffness + _rear_spring_stiffness
    arb_front = 1 + 64 * (_front_spring_stiffness / total_stiffness)
    arb_rear = 1 + 64 * (_rear_spring_stiffness / total_stiffness)
    return arb_front, arb_rear
