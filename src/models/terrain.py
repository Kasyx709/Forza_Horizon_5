from src.base_class.base_class import TuneBase
from src.core.terrain import terrain_type


class Terrain(TuneBase):
    terrain:str
    def __init__(self, terrain:str):
        super().__init__(terrain=terrain)


    def set_terrain_type(self) -> None:
        if terrain_type in terrain_type:
            setattr(self, "terrain_type", terrain_type(self.terrain))
        else:
            raise ValueError(f"Invalid terrain type {terrain_type}")

    @staticmethod
    def terrain_modifier(terrain_type, drivetrain, value):
        """
        :param terrain_type:
        :param drivetrain:
        :param value:
        :return:
        """
        terrain_multiplier = {
            "dirt", 0.95,
            "snow", 0.95
        }

        return terrain_type[terrain_multiplier]
