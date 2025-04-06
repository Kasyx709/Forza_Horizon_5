"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""

import pandas

from models import BaseVehicle, VehicleCategory, Terrain
from suspension import calc_suspension


class Vehicle(BaseVehicle, VehicleCategory, Terrain):
    """
    Create custom tuning parameters for a vehicle in Forza Horizon 5 using real world tuning parameters
    :param vehicle_year: Year of vehicle
    :param vehicle_make: Make of vehicle
    :param vehicle_model: Model of vehicle
    :param vehicle_weight:
    :param front_height:
    :param rear_height:
    :param weight_distribution:
    :param engine_location:
    :param drivetrain:
    :param terrain_types: "cross-country","dirt", "road","snow","race"
    :return:
    """

    def vehicle_attributes(self):
        for k in self.__dict__:
            print(k, self.__getattribute__(k))

    def set_weight_distribution(self):
        setattr(self, "weight_distribution", self.weight_distribution * 0.01)

    def vehicle_suspension(self):
        suspension_settings = calc_suspension(self)
        for k in suspension_settings.__dict__:
            if not k == 'vehicle':
                v = suspension_settings.__getattribute__(k)
                if isinstance(v, float):
                    v = round(v, 1)
                self.__dict__[k] = v
                print(k, v)
        del suspension_settings

    @staticmethod
    def vehicle_class(vehicle_model_year):
        sheet_id = '1yucDOQ2nRaCcC4y4unl72Um7N_pQXuaI6gZqzf0Tl3M'
        sheet_name = 'Cars'
        car_data = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"

        cars = pandas.read_csv(car_data)
        cars = cars[cars.columns[3:]]
        cars.rename({
            cars.columns[0]: "Year"
            , cars.columns[1]: "Make"
            , cars.columns[2]: "Model"
        }
            , axis='columns'
            , inplace=True)
        cars.dropna(axis=1, how='all', inplace=True)
        cars.dropna(axis=0, how='all', inplace=True)
        cars.reset_index(drop=True, inplace=True)
        cars = cars[cars["Year"].isin(vehicle_model_year["vehicle_year"])]
        cars = cars[cars["Model"].str.lower().isin(vehicle_model_year["vehicle_model"].lower())]
        cars = cars[cars["Make"].str.lower().isin(vehicle_model_year["vehicle_make"].lower())]
        cars.set_index(["Year", "Make", "Model", "Car Type"], inplace=True, drop=True)
        if not cars.empty:
            return cars.index[0]


if __name__ == '__main__':
    pass
