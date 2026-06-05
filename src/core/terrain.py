from typing import Set

terrain_types: Set = {
        "cross-country",
        "dirt",
        "road",
        "snow",
        "track"
    }

def terrain_modifier(terrain, drivetrain, value):
    """
    :param terrain:
    :param drivetrain:
    :param value:
    :return:
    """
    terrain_multiplier = {
        "dirt", 0.95,
        "snow", 0.95
    }

    return terrain[terrain_multiplier]
