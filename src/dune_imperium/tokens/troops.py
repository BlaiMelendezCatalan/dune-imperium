from enum import Enum
from pydantic import BaseModel


class TroopState(int, Enum):

    SUPPLY = 1
    GARRISON = 2
    CONFLICT = 3


class Troop(BaseModel):

    state: TroopState = TroopState.SUPPLY
