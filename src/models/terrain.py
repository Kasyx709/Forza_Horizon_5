from typing import Set

from pydantic import BaseModel

terrain_types: Set = {
    "cross-country",
    "dirt",
    "road",
    "snow",
    "race"
}


class BaseTerrain(BaseModel):
    terrain_type: str

    def set_terrain_type(self, terrain_type: str) -> None:
        if terrain_type in terrain_types:
            setattr(self, "terrain_type", terrain_type)
        else:
            raise ValueError(f"Invalid terrain type {terrain_type}")
