from typing import TypeAlias, final, Literal
from pydantic import Field
from .basis_config import BasisConfigLog, BasisConfigUniform
from .forzen_config import FrozenBaseModel

Theory: TypeAlias = Literal["ofdft", 'ksdft']
Potential: TypeAlias = Literal["ae"]


@final
class SystemConfig(FrozenBaseModel):
    basis_conf: BasisConfigLog | BasisConfigUniform = Field(...,
                                                             description="basis")
