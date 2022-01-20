"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from vehicle import Vehicle


def build_vehicle(v_name, v_yr, v_wt, f_h, r_ht, f_wt_pct, dtrain, t_type):
    return Vehicle(v_name, v_yr, v_wt, f_h, r_ht, f_wt_pct, dtrain, t_type)


if __name__ == '__main__':
    vehicle_name = "Superlight R500"
    vehicle_year = 2015
    vehicle_weight = 3228
    front_height = 4.2
    rear_height = 5
    front_wt_pct = 55
    drivetrain = "rwd"
    terrain_type = "road"
    vehicle = build_vehicle(
        vehicle_name,
        vehicle_year,
        vehicle_weight,
        front_height, rear_height,
        front_wt_pct,
        drivetrain,
        terrain_type
    )
    vehicle.vehicle_attributes()
