def differential(weight_percent_front, spring_multi):
    diff_setting = (100 / weight_percent_front) * spring_multi
    return diff_setting if diff_setting <= 100 else 100
