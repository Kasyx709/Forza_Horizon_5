# Conversion from Weight -> mass = Weight / 32.2 | 32.5 = half of 65

_antirollbar_modifier: float = 32.5


def antiroll_bar(_front_spring: float, _rear_spring, front_bias, track_length: int):
    _front_spring_stiffness = (2 * _front_spring) * (track_length / 2) ** 2
    _rear_spring_stiffness = (2 * _rear_spring) * (track_length / 2) ** 2
    _target_front_bias = (front_bias / 100) + 0.05
    total_stiffness = _front_spring_stiffness + _rear_spring_stiffness
    _front_bias_pct = round(_front_spring_stiffness / total_stiffness, 2)
    _offset = round(_front_bias_pct - _target_front_bias, 2)
    arb_front = 1 + 64 * (_front_spring_stiffness / total_stiffness)
    arb_rear = 1 + 64 * (_rear_spring_stiffness / total_stiffness)
    if _offset > 0:
        arb_front = arb_front + (arb_front * _offset)
        arb_rear = arb_rear + -1 * (arb_rear * _offset)
    else:
        arb_front = arb_front + -1 * (arb_front * _offset)
        arb_rear = arb_rear + (arb_rear * _offset)
    return arb_front, arb_rear
