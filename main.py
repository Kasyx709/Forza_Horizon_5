"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from vehicle import Vehicle


def build_vehicle(v_mk_mdl, v_yr, v_wt, f_h, r_ht, f_wt_pct, dtrain, t_type):
    return Vehicle(v_mk_mdl, v_yr, v_wt, f_h, r_ht, f_wt_pct, dtrain, t_type)


if __name__ == '__main__':
    vehicle_make_model = "Zenvo", "TS1"
    vehicle_year = 2016
    vehicle_weight = 3228
    front_height = 3.7
    rear_height = 3.2
    front_wt_pct = 46
    drivetrain = "awd"
    terrain_type = "race"
    vehicle = build_vehicle(
        vehicle_make_model,
        vehicle_year,
        vehicle_weight,
        front_height, rear_height,
        front_wt_pct,
        drivetrain,
        terrain_type
    )
    vehicle.vehicle_attributes()