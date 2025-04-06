from typing import Set, List, Dict, Optional

from pydantic import BaseModel

categories: List = [
    'Buggies', 'Classic Muscle', 'Classic Racers', 'Classic Rally', 'Classic Sports Cars', 'Cult Cars',
    'Drift Cars', 'Extreme Track Toys', 'GT Cars', 'Hot Hatch', 'Hypercars', 'Modern Muscle',
    'Modern Rally', 'Modern Sports Cars', 'Modern Supercars', 'Offroad', 'Pickups & 4x4s',
    'Rally Monsters', 'Rare Classics', 'Retro Hot Hatch', 'Retro Muscle', 'Retro Rally',
    'Retro Saloons', 'Retro Sports Cars', 'Retro Supercars', 'Rods and Customs',
    'Sports Utility Heroes', 'Super GT', 'Super Hot Hatch', 'Super Saloons',
    'Track Toys', 'Trucks', "UTV", 'Unlimited Buggies', 'Unlimited Offroad',
    'Vans & Utility', 'Vintage Racers'
]
terrain_types: Set = {
    "cross-country",
    "dirt",
    "road",
    "snow",
    "race"
}


class Terrain:
    terrain_type: str

    def set_terrain_type(self, terrain_type: str) -> None:
        if terrain_type in terrain_types:
            setattr(self, "terrain_type", terrain_type)
        else:
            raise ValueError(f"Invalid terrain type {terrain_type}")


class VehicleCategory:
    category: str

    def set_category(self, category: str) -> None:
        if category in categories:
            setattr(self, "category", self.category)
        else:
            raise ValueError(f"Invalid terrain type {category}")


class BaseVehicle(BaseModel):
    vehicle_year: Optional[int]
    vehicle_make: Optional[str]
    vehicle_model: Optional[str]
    vehicle_weight: int
    front_height: float
    rear_height: float
    weight_distribution: float
    engine_location: str
    drivetrain: str
    terrain_type: str = None
    category: str = None
