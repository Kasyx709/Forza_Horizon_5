"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from vehicle import Vehicle
from typing import Optional, LiteralString, List


def build_vehicle(
        vehicle_make_model: Optional[LiteralString, List]
        , vehicle_year: int
        , vehicle_weight: int
        , front_height: float
        , rear_height: float
        , front_weight_percentage: int
        , engine_location: str
        , drivetrain_type: str
        , terrain_type: str):
    """

    :param vehicle_make_model:
    :param vehicle_year:
    :param vehicle_weight:
    :param front_height:
    :param rear_height:
    :param front_weight_percentage:
    :param engine_location:
    :param drivetrain_type:
    :param terrain_type: "cross-country","dirt", "road","snow","race"
    :return:
    """
    return Vehicle(vehicle_make_model, vehicle_year, vehicle_weight, front_height, rear_height, front_weight_percentage,
                   engine_location, drivetrain_type, terrain_type)


if __name__ == '__main__':
    vehicle = build_vehicle(
        vehicle_make_model=["RX", "TSC"]
        , vehicle_year=1965
        , vehicle_weight=2613
        , front_height=5.7
        , rear_height=5.6
        , front_weight_percentage=54
        , drivetrain_type="rwd"
        , engine_location="front"
        , terrain_type="dirt"
    )
    vehicle.vehicle_attributes()
