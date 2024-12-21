from abc import ABC, abstractmethod
from dune_imperium.icons import AgentIcon
from dune_imperium.map.control import Control, SpiceControl


class Location(ABC):

    name: str
    agent_icon: AgentIcon
    combat: bool = False
    control: Control | None = None
    free: bool = True

    @abstractmethod
    def pay(self, player_id: int) -> None:
        pass

    @abstractmethod
    def reward(self, player_id: int) -> None:
        pass


class SpiceLocation(Location):

    extra_spice: int = 0

    @abstractmethod
    def produce_spice(self) -> None:
        pass


class Arrakeen(Location):

    name = "arrakeen"
    agent_icon = AgentIcon.CITY
    combat = True

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO Petition to API to increase player_id troop by 1 and drawing card
        ...


class ImperialBasin(SpiceLocation):

    name = "imperial_basin"
    agent_icon = AgentIcon.SPICE_TRADE
    combat = True
    control = SpiceControl()

    def pay(self, player_id: int) -> None:
        # TODO for other locations where pay is needed, this calls API to modify player resources or
        # to say payment was not successful
        return

    def reward(self, player_id: int) -> None:
        # TODO Petition to API to increase player_id spice with (1 + self.extra_spice)
        self.extra_spice = 0

    def produce_spice(self):
        self.extra_spice += 1
