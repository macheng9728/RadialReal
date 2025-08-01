from typing import final, Literal, TypeAlias, Tuple
from pydantic import Field, model_validator

from .forzen_config import FrozenBaseModel


@final
class SolverConfigDEM(FrozenBaseModel):
    solver: Literal["dem"]
    max_loop: int = Field(ge=1, description="The maximum number of iterations")
    method: Literal["lbfgs", "cg", "tn"] = Field(default="tn",
                                                 description="The solver method")

@final
class SolverConfigOESCF(FrozenBaseModel):
    solver: Literal["oescf"]
