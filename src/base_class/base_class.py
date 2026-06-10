from pydantic import BaseModel, ConfigDict


class TuneBase(BaseModel):
    drivetrain_type: str
    purpose: str
    weight: int
    weight_distribution_pct: float
    model_config = ConfigDict(str_to_lower=True)
