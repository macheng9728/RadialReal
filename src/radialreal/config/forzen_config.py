from pydantic import BaseModel

class FrozenBaseModel(BaseModel):
    class Config:
        frozen = True