_antirollbar_modifier: float = 35


def antiroll_bar(spring_rate: float, is_track: bool = False, is_rear: bool = False,
                 antirollbar_modifier: float = _antirollbar_modifier):
    _arb = spring_rate / antirollbar_modifier
    if is_track:
        _arb = _arb * 1.4
    if not is_rear:
        _arb = _arb * 1.2
    return _arb
