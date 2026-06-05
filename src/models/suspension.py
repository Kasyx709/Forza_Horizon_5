from typing import Dict, Set
from typing import Optional

from src.core.antiroll import antiroll_bar
from src.core.spring import spring_rate, track_spring_rate


class Suspension:
    antirollbar_front: float
    antirollbar_rear: float
    stiffness_spring_front: float
    stiffness_spring_rear: float
    damper_rebound_front: float
    damper_rebound_rear: float
    damper_bump_front: float
    damper_bump_rear: float
    damper_rebound_max: int = 40
    damper_bump_max: int = 40
    bump_modifier: float = 0.65
    antirollbar_modifier: float = 35
    track_type_modifier: float = 2.0
    natural_frequency_range: Dict = {
        1: (1.4, 2.0),  # Rally Cars
        2: (1.5, 2.5),  # Non-Aero racecars, moderate downforce Formula cars
        3: (2.5, 3.5),  # Moderate downforce racecars with up to 50% total weight in max downforce capability
        4: (3.5, 5.0),  # High downforce racecars with more than 50% of their weight in max downforce
    }
    _natural_frequency_range: tuple
    forza_tune_categories: Set = {
        "Roll bar",
        "Spring",
        "Rebound",
        "Bump",
        "Differential"
    }
    spring_type_modifier: Dict = {
        "standard": 1.0,
        "track": 2.0,
    }
    is_track: bool = False
    spring_type: str
    spring_multiplier: float
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

    def set_spring_type_modifier(self):
        setattr(self, "spring_multiplier", self.spring_type_modifier[self.spring_type])
        if self.spring_multiplier == 2:
            setattr(self, "is_track", True)

    def set_frequency_range(self, weight_class):
        setattr(self, "_natural_frequency_range", self.natural_frequency_range[weight_class])

    def set_spring_stiffness(self, weight, weight_distribution_pct, is_rear=False) -> None:
        if is_rear:
            setattr(self, "stiffness_spring_rear",
                    spring_rate(self._natural_frequency_range, weight, weight_distribution_pct,
                                self.spring_multiplier,
                                is_rear=True))
        else:
            setattr(self, "stiffness_spring_front",
                    spring_rate(self._natural_frequency_range, weight, weight_distribution_pct,
                                self.spring_multiplier))

    def adjust_track_spring_rate_by_weight(self, weight):
        if self.is_track:
            setattr(self, "stiffness_spring_front", track_spring_rate(weight, self.stiffness_spring_front))
            setattr(self, "stiffness_spring_rear", track_spring_rate(weight, self.stiffness_spring_rear))

    def set_damper_rebound(self, weight):
        setattr(self, "damper_rebound_front", self.damper_rebound_max * (self.stiffness_spring_front / weight))
        setattr(self, "damper_rebound_rear", self.damper_rebound_max * (self.stiffness_spring_rear / weight))

    def set_damper_bump(self):
        setattr(self, "damper_bump_front", self.damper_rebound_front * self.bump_modifier)
        setattr(self, "damper_bump_rear", self.damper_rebound_rear * self.bump_modifier)

    def set_antiroll_bar(self, drivetrain_type):
        _arb = [antiroll_bar(self.stiffness_spring_front, is_track=self.is_track),
                antiroll_bar(self.stiffness_spring_rear, is_track=self.is_track, is_rear=True)]
        if drivetrain_type != 2:
            setattr(self, "antirollbar_front", _arb[0])
            setattr(self, "antirollbar_rear", _arb[1])
        else:
            setattr(self, "antirollbar_front", _arb[1])
            setattr(self, "antirollbar_rear", _arb[0])
        del _arb

    def vehicle_suspension(self):
        for k in self.__dict__:
            if k in self.suspension_values:
                v = self.__getattribute__(k)
                if isinstance(v, float):
                    v = round(v, 1)
                self.suspension_values[k] = v
                print(k, v)
