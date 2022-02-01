"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""

from suspension import calc_suspension
import pandas as pd

pd.set_option('max_rows', 1000)


class Vehicle(object):
    car_types = [
        'Buggies', 'Classic Muscle', 'Classic Racers', 'Classic Rally', 'Classic Sports Cars', 'Cult Cars',
        'Drift Cars', 'Extreme Track Toys', 'GT Cars', 'Hot Hatch', 'Hypercars', 'Modern Muscle',
        'Modern Rally', 'Modern Sports Cars', 'Modern Supercars', 'Offroad', 'Pickups & 4x4s',
        'Rally Monsters', 'Rare Classics', 'Retro Hot Hatch', 'Retro Muscle', 'Retro Rally',
        'Retro Saloons', 'Retro Sports Cars', 'Retro Supercars', 'Rods and Customs',
        'Sports Utility Heroes', 'Super GT', 'Super Hot Hatch', 'Super Saloons',
        'Track Toys', 'Trucks', "UTV's", 'Unlimited Buggies', 'Unlimited Offroad',
        'Vans & Utility', 'Vintage Racers'
    ]

    def __init__(self, vehicle_make_model, vehicle_year, vehicle_weight, front_height, rear_height, front_wt_pct,
                 engine_location, drivetrain, terrain_type):
        self.vehicle_year, self.vehicle_make, self.vehicle_model, self.vehicle_type = vehicle_class(vehicle_make_model,
                                                                                                    vehicle_year)
        self.vehicle_weight: int = vehicle_weight
        self.height_front: float = front_height
        self.height_rear: float = rear_height
        self.weight_percent_front: float = front_wt_pct * 0.01
        self.engine_location: str = engine_location
        self.drivetrain: str = drivetrain
        suspension_settings = calc_suspension(self, engine_location, drivetrain, terrain_type)
        for k in suspension_settings.__dict__:
            if not k == 'vehicle':
                v = suspension_settings.__getattribute__(k)
                if isinstance(v, float):
                    v = round(v, 1)
                    self.__setattr__(k, v)

    def vehicle_attributes(self):
        for k in self.__dict__:
            print(k, self.__getattribute__(k))


def vehicle_class(vehicle_make_model, vehicle_year):
    sheet_id = '1yucDOQ2nRaCcC4y4unl72Um7N_pQXuaI6gZqzf0Tl3M'
    sheet_name = 'Cars'
    car_data = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

    vehicle_make, vehicle_model = vehicle_make_model
    cars = pd.read_csv(car_data)
    cars = cars[cars.columns[3:]]
    cars.rename({cars.columns[0]: "Year", cars.columns[1]: "Make", cars.columns[2]: "Model", }, axis='columns',
                inplace=True)
    cars.dropna(axis=1, how='all', inplace=True)
    cars.dropna(axis=0, how='all', inplace=True)
    cars.reset_index(drop=True, inplace=True)
    cars = cars[cars["Year"].isin([vehicle_year])]
    cars = cars[cars["Model"].str.lower().isin([vehicle_model.lower()])]
    cars = cars[cars["Make"].str.lower().isin([vehicle_make.lower()])]
    cars.set_index(["Year", "Make", "Model", "Car Type"], inplace=True, drop=True)
    if not cars.empty:
        return cars.index[0]
    else:
        return vehicle_year, vehicle_make, vehicle_model, None


if __name__ == '__main__':
    pass
