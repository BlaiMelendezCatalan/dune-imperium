from enum import Enum
from dune_imperium.map.locations import Location


class Agent:

    _deployed: bool = False
    _location: Location | None = None

    def __init__(self, player_id: int):
        self._player_id = player_id

    def deploy(self, location: Location) -> None:
        self._deployed = True
        self._location = location
        self._location.pay(self._player_id)
        # TODO run location methods passing player_id as a parameter
        # - run location.pay or tell user it is not possible
        # - run location.reward
        # - run location.control.add_resource

    def recall(self) -> None:
        self._deployed = False
        self._location = None


class Agents:

    def __init__(self, player_id: int):
        self._agents: list[Agent] = [Agent(player_id) for _ in range(2)]


class TroopState(Enum):

    SUPPLY = 1
    GARRISON = 2
    CONFLICT = 3


class Troop:

    _state: TroopState = TroopState.SUPPLY


class Army:

    _troops: list[Troop] = [Troop() for _ in range(16)]
