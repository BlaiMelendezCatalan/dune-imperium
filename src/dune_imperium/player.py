from dune_imperium.decks.leaders import Leader
from dune_imperium.map.trackers import InfluenceTracker, VictoryPointsTracker
from dune_imperium.tokens import Agents, Troops


class Player:

    _water: int = 1
    _solari: int = 0
    _spice: int = 0

    _troops: Troops = Troops()

    _influence_trackers: dict[str, InfluenceTracker] = {
        name: InfluenceTracker()
        for name in ["fremen", "bene_gesserit", "spacing_guild", "emperor"]
    }

    def __init__(
        self,
        id: int,
        username: str,
        color: str,
        leader: Leader,
        initial_victory_points: int,
        first_player: bool = False,
    ):
        self._id = id
        self._username = username
        self._color = color
        self._leader = leader
        self._agents = Agents(id)
        self._victory_points = VictoryPointsTracker(initial_victory_points)
        self._first_player = first_player

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

    @property
    def troops(self) -> Troops:
        return self._troops

    @property
    def first_player(self) -> bool:
        return self._first_player

    @property
    def influence_trackers(self) -> dict[str, InfluenceTracker]:
        return self._influence_trackers

    @property
    def victory_points(self) -> int:
        return self._victory_points.victory_points
