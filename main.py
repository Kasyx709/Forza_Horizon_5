"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from vehicle import Vehicle

if __name__ == '__main__':
    vehicle = Vehicle(
        vehicle_year=1970
        , vehicle_make="GMC"
        , vehicle_model="Jimmy"
        , vehicle_weight=2449
        , front_height=6.7
        , rear_height=6.8
        , weight_distribution=49
        , drivetrain="rwd"
        , spring_type="race"
    )
    vehicle.set_weight_distribution()
    vehicle.set_terrain_type(terrain_type="cross-country")
    vehicle.vehicle_attributes()
    vehicle.vehicle_suspension()
