from pydantic import BaseModel


class Resources(BaseModel):
    water: int = 1
    solari: int = 0
    spice: int = 0
