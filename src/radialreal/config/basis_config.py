from typing import final, Literal, TypeAlias
from pydantic import Field, model_validator

from .forzen_config import FrozenBaseModel

@final
class BasisConfigLog(FrozenBaseModel):
    basis: Literal["log"]
    r_max: float = Field(gt=0, description="Maximum radius")
    r_min: float = Field(gt=0, description="Minimum radius")
    n_points: int = Field(gt=0, description="Number of points")
    @model_validator(mode='after')
    def check_min_is_less_than_max(self):
        # This check runs after r_min and r_max have been parsed.
        if self.r_max < self.r_min:
            raise ValueError("r_min larger than r_max")
        return self

@final
class BasisConfigUniform(FrozenBaseModel):
    basis: Literal["uniform"]
    r_max: float = Field(gt=0, description="Maximum radius")
    r_min: float = Field(gt=0, description="Minimum radius")
    n_points: int = Field(gt=0, description="Number of points")
    @model_validator(mode='after')
    def check_min_is_less_than_max(self):
        # This check runs after r_min and r_max have been parsed.
        if self.r_max < self.r_min:
            raise ValueError("r_min larger than r_max")
        return self
