from enum import Enum

from pydantic import BaseModel


class TroopState(int, Enum):

    SUPPLY = 1
    GARRISON = 2
    CONFLICT = 3


class Troop(BaseModel):

    state: TroopState = TroopState.SUPPLY

    def to_garrison(self) -> None:
        self.state = TroopState.GARRISON

    def to_conflict(self) -> None:
        self.state = TroopState.CONFLICT

    def to_supply(self) -> None:
        self.state = TroopState.SUPPLY


class TroopPool(BaseModel):

    troops: list[Troop] = [Troop() for _ in range(12)]

    def recruit(self, number: int) -> None:
        for troop in self.supply[:number]:
            troop.to_garrison()

    def deploy(self, number: int, source: str) -> None:
        troops = self.supply if source == "supply" else self.garrison
        for troop in troops[:number]:
            troop.to_conflict()

    def reset(self, number: int | None = None) -> None:
        for troop in self.conflict:
            troop.to_supply()

    def retreat(self, number: int) -> None:
        for troop in self.conflict[:number]:
            troop.to_garrison()

    @property
    def supply(self) -> list[Troop]:
        return [troop for troop in self.troops if troop.state == TroopState.SUPPLY]

    @property
    def garrison(self) -> list[Troop]:
        return [troop for troop in self.troops if troop.state == TroopState.GARRISON]

    @property
    def conflict(self) -> list[Troop]:
        return [troop for troop in self.troops if troop.state == TroopState.CONFLICT]
