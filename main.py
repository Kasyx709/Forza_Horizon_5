"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from vehicle import Vehicle

if __name__ == '__main__':
    vehicle = Vehicle(
        vehicle_year=1965
        , vehicle_make="RX"
        , vehicle_model="TSC"
        , vehicle_weight=2613
        , front_height=5.7
        , rear_height=5.6
        , weight_distribution=54
        , drivetrain="rwd"
        , engine_location="front"
    )
    vehicle.set_weight_distribution()
    vehicle.set_terrain_type(terrain_type="dirt")
    vehicle.vehicle_attributes()
    vehicle.vehicle_suspension()
