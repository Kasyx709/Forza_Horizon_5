"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""


def rebound_stiffness(rebound_max, spring_rate, total_weight):
    _reboun_spring = 1 + 19 * ((spring_rate /total_weight) / 40)
    return rebound_max * (spring_rate / total_weight)


def bump_stiffness(_rebound_stiffness, bump_modifier):
    return _rebound_stiffness * bump_modifier


if __name__ == '__main__':
    pass
