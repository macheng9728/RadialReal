from typing import TypeAlias, final, Literal
from pydantic import Field
from .basis_config import BasisConfigLog, BasisConfigUniform
from .thoery_config import TheoryConfigKSDFT, TheoryConfigOFDFT
from .solver_config import SolverConfigDEM, SolverConfigOESCF
from .potential_config import PotentialConfigAE, PotentialConfigNone
from .forzen_config import FrozenBaseModel


@final
class SystemConfig(FrozenBaseModel):
    basis_conf: BasisConfigLog | BasisConfigUniform = Field(...,
                                                            discriminator="basis")
    theory_conf: TheoryConfigKSDFT | TheoryConfigOFDFT = Field(...,
                                                               discriminator="theory")
    solver_conf: SolverConfigDEM | SolverConfigOESCF = Field(...,
                                                             discriminator="solver")
    potential_conf: PotentialConfigAE | PotentialConfigNone = Field(...,
                                                                    discriminator="potential")
