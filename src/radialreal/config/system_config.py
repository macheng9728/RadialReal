import logging
from collections.abc import Iterator
from typing import TypeAlias

from pydantic import BaseModel, Field
from typing_extensions import final,Literal

Theory: TypeAlias = Literal["ofdft",'ksdft']
Potential = Literal["ae"]
Basis = Literal["log",'uniform']
Solver = Literal["dem","oescf"]

@final
class SystemConfig(BaseModel):
    theory : Theory
    potential : Potential
    basis  : Basis
    solver : Solver

@final
class BasisConfigLog(BaseModel):
    r_max : float = Field(gt=0, description="Minimum radius")
    r_min : float = Field(gt=0,lt=r_max, description="Maximum radius")
    n_points : int = Field(gt=0, description="Number of points")

@final
class BasisConfigFromfile(BaseModel):
    file : str
