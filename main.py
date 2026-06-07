"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from src.core.gears import gear_ratio_calculator
from src.models.vehicle import Vehicle

if __name__ == '__main__':
    # TODO Add in sqlite db that allows for local storing/recalling of previous vehicle configurations.
    spring_type = "track", "standard"
    weight = 2301
    number_of_gears = 4
    rpm_redline = 9200
    vehicle_torque = 1347
    weight_distribution_pct = 43
    turbo_psi = 14.7
    tire_size = {385, 30, 18}
    final_drive_ratio = 2.6
    drivetrain_type = "RWD"
    terrain_type = "track"
    tire_compound = "Slick"
    vehicle = Vehicle(
        weight=weight
        , weight_distribution_pct=weight_distribution_pct
        , drivetrain_type=drivetrain_type
        , terrain_type=terrain_type
        , spring_type=spring_type[0])
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
    gears = gear_ratio_calculator(
        weight
        , vehicle_torque
        , drivetrain_type
        , rpm_redline
        , number_of_gears
        , tire_compound
        , tire_size
        , final_drive_ratio
        , turbo_psi
    )
    print(gears)
