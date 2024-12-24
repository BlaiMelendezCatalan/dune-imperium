from abc import ABC, abstractmethod
from pydantic import BaseModel

from dune_imperium.icons import AgentIcon
from dune_imperium.map.control import Control, SolariControl, SpiceControl
from dune_imperium.tokens.resources import Resources


class Cost(BaseModel):

    resources: dict[Resources, int] = {}
    fremen_influence: int = 0


class Location(BaseModel, ABC):

    name: str
    agent_icon: AgentIcon
    combat: bool = False
    control: Control | None = None
    cost: Cost = Cost()
    free: bool = True

    @abstractmethod
    def pay(self, player_id: int) -> None:
        # TODO This calls API to modify game state (player resources) or to say payment was not successful
        pass

    @abstractmethod
    def reward(self, player_id: int) -> None:
        # TODO This calls API to modify game state (player resources, troop deployment, influence, aliance tokens, ...)
        pass


class SpiceLocation(Location):

    extra_spice: int = 0

    def produce_spice(self):
        self.extra_spice += 1

    @abstractmethod
    def pay(self, player_id: int) -> None:
        pass

    @abstractmethod
    def reward(self, player_id: int) -> None:
        pass


class Arrakeen(Location):

    name = "arrakeen"
    agent_icon = AgentIcon.CITY
    combat = True
    control = SolariControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Carthag(Location):

    name = "carthag"
    agent_icon = AgentIcon.CITY
    combat = True
    control = SolariControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Conspire(Location):

    name = "conspire"
    agent_icon = AgentIcon.EMPEROR

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class FoldSpace(Location):

    name = "fold_space"
    agent_icon = AgentIcon.SPACING_GUILD

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class TheGreatFlat(SpiceLocation):

    name = "the_great_flat"
    agent_icon = AgentIcon.SPICE_TRADE
    combat = True

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HaggaBasin(SpiceLocation):

    name = "hagga_basin"
    agent_icon = AgentIcon.SPICE_TRADE
    combat = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        self.extra_spice = 0


class HallOfOratory(Location):

    name = "hall_of_oratory"
    agent_icon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HardyWarriors(Location):

    name = "hardy_warriors"
    agent_icon = AgentIcon.FREMEN
    combat = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Heighliner(Location):

    name = "heighliner"
    agent_icon = AgentIcon.SPACING_GUILD
    combat = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HighCouncil(Location):

    name = "high_council"
    agent_icon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class ImperialBasin(SpiceLocation):

    name = "imperial_basin"
    agent_icon = AgentIcon.SPICE_TRADE
    combat = True
    control = SpiceControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        self.extra_spice = 0


class Mentat(Location):

    name = "mentat"
    agent_icon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class RallyTroops(Location):

    name = "rally_troops"
    agent_icon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class ResearchStation(Location):

    name = "research_location"
    agent_icon = AgentIcon.CITY
    combat = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Secrets(Location):

    name = "secrets"
    agent_icon = AgentIcon.BENE_GESSERIT

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SecureContract(Location):

    name = "secure_contract"
    agent_icon = AgentIcon.SPICE_TRADE

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SelectiveBreeding(Location):

    name = "selective_breeding"
    agent_icon = AgentIcon.BENE_GESSERIT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SellMelange(Location):

    name = "sell_melange"
    agent_icon = AgentIcon.SPICE_TRADE

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SietchTabr(Location):

    name = "sietch_tabr"
    agent_icon = AgentIcon.CITY
    combat = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Stillsuits(Location):

    name = "stillsuits"
    agent_icon = AgentIcon.FREMEN
    combat = True

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Swordmaster(Location):

    name = "swordmaster"
    agent_icon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Wealth(Location):

    name = "wealth"
    agent_icon = AgentIcon.EMPEROR

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Locations(BaseModel):

    locations: list[Location] = []

    def __init__(self, **data) -> None:
        super.__init__(**data)
        self.locations = [
            subclass()  # pyright: ignore[reportCallIssue]
            for subclass in Location.__subclasses__()
            if subclass is not SpiceLocation
        ]
        self.locations += [
            subclass()  # pyright: ignore[reportCallIssue]
            for subclass in SpiceLocation.__subclasses__()
        ]
