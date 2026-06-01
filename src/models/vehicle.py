from typing import Optional, List

from pydantic import BaseModel

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


class BaseVehicle(BaseModel):
    vehicle_year: Optional[int]
    vehicle_make: Optional[str]
    vehicle_model: Optional[str]
    vehicle_weight: int
    front_height: float
    rear_height: float
    weight_distribution: float
    drivetrain: str
    terrain_type: str = None
    category: str = None


class BaseVehicleCategory(BaseModel):
    spring_type: str
    vehicle_categories: List = vehicle_categories
