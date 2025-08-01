from typing import final, Literal, TypeAlias, Tuple
from pydantic import Field, model_validator

from .forzen_config import FrozenBaseModel


@final
class TheoryConfigOFDFT(FrozenBaseModel):
    theory: Literal["ofdft"]
    kedf: Literal["tf", "vw", "lkt"] = Field(
        description="Kinetic energy density function")
    xc: Literal["lda", "pbe"] = Field(
        description="exchange correlation functional")
    coulomb: Literal["all", "none", "radio"] = Field(
        description="coulomb energy", default="all")
    e_tolerance: float = Field(gt=0, description="energy tolerance in Ha",
                               default=1e-6)
    kedf_parameters : Tuple[float, ...] = Field(
        description="An array of custom floating-point values.",
        default_factory=tuple)
@final
class TheoryConfigKSDFT(FrozenBaseModel):
    theory: Literal["ksdft"]
    xc: Literal["lda", "pbe"] = Field(
        description="exchange correlation functional")
