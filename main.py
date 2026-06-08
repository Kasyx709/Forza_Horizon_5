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
    weight = 1588
    number_of_gears = 6
    rpm_redline = 7500
    vehicle_torque = 845
    weight_distribution_pct = 49
    turbo_psi = 0
    tire_size = {285, 50, 15}
    final_drive_ratio = 2.3
    drivetrain_type = "RWD"
    purpose = "rickybobby"
    tire_compound = "Semislick"
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
    vehicle.set_antiroll_bar(vehicle.drivetrain_type, weight_distribution_pct)
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
