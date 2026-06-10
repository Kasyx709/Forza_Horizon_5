"""/* Copyright (C) Richard Custureri - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary
 * Written by Richard Custureri <Rick.Custureri@gmail.com>, January 2022
 */
"""
from typing import List, Dict, Optional

import pandas

from src.base_class.base_class import TuneBase
from src.models.suspension import Suspension


class VehicleCategory:
    """
    :param year: Year of vehicle
    :param make: Make of vehicle
    :param model: Model of vehicle
    :param category: Type of Vehicle
    :return:
    """
    year: Optional[int]| None = None
    make: Optional[str]| None = None
    model: Optional[str]| None = None
    category: Optional[str]| None = None

    vehicle_categories: List = [
        'Buggies', 'Classic Muscle', 'Classic Racers', 'Classic Rally', 'Classic Sports Cars', 'Cult Cars',
        'Drift Cars', 'Extreme Track Toys', 'GT Cars', 'Hot Hatch', 'Hypercars', 'Modern Muscle',
        'Modern Rally', 'Modern Sports Cars', 'Modern Supercars', 'Offroad', 'Pickups & 4x4s',
        'Rally Monsters', 'Rare Classics', 'Retro Hot Hatch', 'Retro Muscle', 'Retro Rally',
        'Retro Saloons', 'Retro Sports Cars', 'Retro Supercars', 'Rods and Customs',
        'Sports Utility Heroes', 'Super GT', 'Super Hot Hatch', 'Super Saloons',
        'Track Toys', 'Trucks', "UTV", 'Unlimited Buggies', 'Unlimited Offroad',
        'Vans & Utility', 'Vintage Racers'
                          'Hypercar'
    ]

    @classmethod
    def set_category(cls, vehicle_category: str) -> None:
        if vehicle_category in cls.vehicle_categories:
            setattr(cls, "category", vehicle_category)
        else:
            raise ValueError(f"Invalid vehicle type {vehicle_category}")

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

class Vehicle(Suspension, VehicleCategory,TuneBase):
    """
    Create custom tuning parameters for a vehicle in Forza Horizon using real world tuning parameters
    :param year: Year of vehicle
    :param make: Make of vehicle
    :param model: Model of vehicle
    :param weight: Weight of vehicle
    :param weight_distribution_pct:
    :param drivetrain_type: All-wheel Drive (AWD), Rear-wheel Drive (RWD), Front-Wheel Drive (FWD)
    :param purpose: "cross-country","dirt", "road","snow","race"
    :return:
    """
    drivetrain_types: Dict[str, str] = {
        "AWD": 1,
        "RWD": 2,
        "FWD": 3,
    }

    def vehicle_attributes(self):
        for k in self.__dict__:
            print(k, self.__getattribute__(k))

    def set_drivetrain_type(self):
        setattr(self, "drivetrain_type", self.drivetrain_types[self.drivetrain_type])




if __name__ == '__main__':
    pass
