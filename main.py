# Calculates suspension settings using 2.8875 constant
# 2.8875/([front+rear height]/2)=spring rate total/2 weight.


def _weight_distribution():
    front_weight = front_weight_pct * total_weight
    rear_weight = total_weight - front_weight
    return front_weight, rear_weight


def _spring_settings(front_weight, rear_weight):
    spring_multi = spring_constant / (front_height + rear_height / 2)
    front_spring = (spring_multi * front_weight)
    rear_spring = (spring_multi * rear_weight) \
                  * (1.25 if front_weight_pct >= 45 else 1.3)
    if rear_spring >= total_weight //2:
        rear_spring = total_weight//2
    return (front_spring, rear_spring), spring_multi


def _damper_settings(spring_multi):
    rebound_multi = 20 * spring_multi
    front_rebound = rebound_multi * front_weight_pct
    front_bump = front_rebound * front_weight_pct  # 0.5
    rear_rebound = rebound_multi * (1 - front_weight_pct)
    rear_bump = rear_rebound * 0.7
    return front_rebound, front_bump, rear_rebound, rear_bump


def _arb_settings(spring_multi):
    arb_multi = 65 * spring_multi
    front_arb = (arb_multi * front_weight_pct) * 0.73
    rear_arb = (arb_multi * (1 - front_weight_pct)) * (1 if front_weight_pct >= 45 else 1.15)
    return front_arb, rear_arb


def _diff_settings(spring_multi):
    diff_setting = (100 / front_weight_pct) * spring_multi
    return diff_setting if diff_setting <= 100 else 100


def calc_suspension():
    front_weight, rear_weight = _weight_distribution()
    spring_settings, spring_multi = _spring_settings(front_weight, rear_weight)
    arb_settings = _arb_settings(spring_multi)
    damper_settings = _damper_settings(spring_multi)
    diff_settings = _diff_settings(spring_multi),
    suspension_values = arb_settings, spring_settings, damper_settings, diff_settings
    return '\n'.join([str([round(x, 1) for i in suspension_values for x in i])])


if __name__ == '__main__':
    spring_constant: float = 2.8875
    total_weight = 3237
    front_weight_pct = 44 * .01
    front_height =3
    rear_height = 2.7
    suspension_settings = calc_suspension()
    print(suspension_settings)
