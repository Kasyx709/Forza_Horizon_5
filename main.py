"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from src.models.vehicle import Vehicle

if __name__ == '__main__':
    # TODO Add in sqlite db that allows for local storing/recalling of previous vehicle configurations.
    spring_type = "track"
    #spring_type = "standard"
    vehicle = Vehicle(
        weight=2013
        , weight_distribution_pct=37
        , drivetrain_type="rwd"
        , terrain_type="track"
        , spring_type=spring_type)
    vehicle.set_track_flag()
    vehicle.set_spring_type_modifier()
    vehicle.set_frequency_range(vehicle.weight_class)
    vehicle.set_spring_stiffness(vehicle.weight, vehicle.weight_distribution_pct)
    vehicle.set_spring_stiffness(vehicle.weight, vehicle.weight_distribution_pct, is_rear=True)
    vehicle.adjust_track_spring_rate_by_weight(vehicle.weight)
    vehicle.set_damper_rebound(vehicle.weight)
    vehicle.set_damper_bump()
    vehicle.set_antiroll_bar(vehicle.drivetrain_type)
    vehicle.vehicle_suspension()