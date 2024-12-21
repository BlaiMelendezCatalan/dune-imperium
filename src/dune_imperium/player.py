from dune_imperium.decks.leaders import Leader
from dune_imperium.tokens import Agents, Army


class Player:

    _water: int = 1
    _solari: int = 0
    _spice: int = 0

    _army: Army = Army()

    def __init__(self, id: int, username: str, color: str, leader: Leader):
        self._id = id
        self._username = username
        self._color = color
        self._leader = leader
        self._agents: Agents = Agents(id)

    @property
    def water(self) -> int:
        return self._water

    @water.setter
    def water(self, value: int) -> None:
        self._water = value

    @property
    def solari(self) -> int:
        return self._solari

    @solari.setter
    def solari(self, value: int) -> None:
        self._solari = value

    @property
    def spice(self) -> int:
        return self._spice

    @spice.setter
    def spice(self, value: int) -> None:
        self._spice = value
