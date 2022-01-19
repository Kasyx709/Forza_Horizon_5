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
    vehicle_name = "morris"
    vehicle_year = 1958
    vehicle_weight = 1543
    front_height = 4.7
    rear_height = 5.5
    front_wt_pct = 53
    drivetrain = "fwd"
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
