from typing import final, Literal, TypeAlias, Tuple
from pydantic import Field, model_validator

from .forzen_config import FrozenBaseModel

@final
class PotentialConfigAE(FrozenBaseModel):
    """
    AE means all electron potential
    - Z/r
    """
    potential : Literal["ae"]
    zion : int = Field(gt=0,description="Zion index")

class PotentialConfigNone(FrozenBaseModel):
    """
    None means none external potential
    """
    potential : Literal["none"]
