from typing import Dict, Set
from typing import Optional

from src.core.antiroll import antiroll_bar
from src.core.spring import spring_rate


class Suspension:
    antirollbar_front: float
    antirollbar_rear: float
    stiffness_spring_front: float
    stiffness_spring_rear: float
    damper_rebound_front: float
    damper_rebound_rear: float
    damper_bump_front: float
    damper_bump_rear: float
    damper_rebound_max: int = 20
    bump_modifier: float = 0.65
    antirollbar_modifier: float = 35
    track_type_modifier: float = 2.0
    natural_frequency_range: Dict = {
        "dirt": (1, 1.8),
        "rally": (1.4, 2.0),  # Rally Cars
        "street": (1.5, 2.5),  # Performance Based Sports Cars
        "track": (2.5, 3.5),  # Non-Aero racecars, moderate downforce Formula cars
        "race": (3, 4.5),  # Moderate downforce racecars with up to 50% total weight in max downforce capability
        "rickybobby": (4.5, 6.0),  # High downforce racecars with more than 50% of their weight in max downforce
        "test": (2.5, 6)
    }
    _natural_frequency_range: tuple
    forza_tune_categories: Set = {
        "Roll bar",
        "Spring",
        "Rebound",
        "Bump",
        "Differential"
    }

    is_track: bool = False
    spring_type: str
    front_height: Optional[float]
    rear_height: Optional[float]
    suspension_values: Dict = {
        "antirollbar_front": None,
        "antirollbar_rear": None,
        "stiffness_spring_front": None,
        "stiffness_spring_rear": None,
        "damper_rebound_front": None,
        "damper_rebound_rear": None,
        "damper_bump_front": None,
        "damper_bump_rear": None,
    }

    def set_frequency_range(self, purpose):
        setattr(self, "_natural_frequency_range", self.natural_frequency_range[purpose])

    def set_spring_stiffness(self, weight, weight_distribution_pct) -> None:
        _softer_spring, _stiffer_spring = spring_rate(self._natural_frequency_range, weight, weight_distribution_pct)
        if weight_distribution_pct < 50:
            setattr(self, "stiffness_spring_front", _stiffer_spring)
            setattr(self, "stiffness_spring_rear", _softer_spring)

        else:
            setattr(self, "stiffness_spring_front", _softer_spring)
            setattr(self, "stiffness_spring_rear", _stiffer_spring)

    def set_damper_rebound(self, weight):
        setattr(self, "damper_rebound_front", 1 + 19 * (self.stiffness_spring_front / weight))
        setattr(self, "damper_rebound_rear", 1 + 19 * (self.stiffness_spring_rear / weight))
        # setattr(self, "damper_rebound_rear", 2 * self.damper_rebound_max * (self.stiffness_spring_rear / weight))

    def set_damper_bump(self):
        setattr(self, "damper_bump_front", self.damper_rebound_front * self.bump_modifier)
        setattr(self, "damper_bump_rear", self.damper_rebound_rear * self.bump_modifier)

    def set_antiroll_bar(self, weight_distribution_pct: int, track_length: int):
        _arb = antiroll_bar(self.stiffness_spring_front, self.stiffness_spring_rear, weight_distribution_pct,
                            track_length=track_length)
        setattr(self, "antirollbar_front", _arb[0])
        setattr(self, "antirollbar_rear", _arb[1])
        del _arb

    def vehicle_suspension(self):
        for k in self.__dict__:
            if k in self.suspension_values:
                v = self.__getattribute__(k)
                if isinstance(v, float):
                    v = round(v, 1)
                self.suspension_values[k] = v
                print(k, v)
