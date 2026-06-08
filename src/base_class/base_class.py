from typing import Optional, TYPE_CHECKING


class _Base:
    pass


if TYPE_CHECKING:
    class TuneBase(_Base):
        year: Optional[int]
        make: Optional[str]
        model: Optional[str]
        weight: int
        purpose: int
        vehicle_category: str
        weight_distribution_pct: float
        drivetrain_type: str
        terrain_type: str
        spring_type: str
else:
    TuneBase = _Base
