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
    weight = 2449
    number_of_gears = 4
    rpm_redline = 4000
    vehicle_torque = 462
    weight_distribution_pct = 52
    turbo_psi = 0.7
    tire_size = {280, 30, 18.5}
    final_drive_ratio = 2.2
    drivetrain_type = "AWD"
    purpose = "dirt"
    tire_compound = "Slick"
    track_length = 60
    vehicle = Vehicle(
        weight=weight
        , weight_distribution_pct=weight_distribution_pct
        , drivetrain_type=drivetrain_type
        , purpose=purpose
    )
    vehicle.set_frequency_range(vehicle.purpose)
    vehicle.set_spring_stiffness(vehicle.weight, vehicle.weight_distribution_pct)
    vehicle.set_damper_rebound(vehicle.weight)
    vehicle.set_damper_bump()
    vehicle.set_antiroll_bar(weight_distribution_pct, track_length=track_length)
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
