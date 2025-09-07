from pydantic import BaseModel

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.map.control import Control, SolariControl, SpiceControl


class Cost(BaseModel):

    water: int = 0
    solari: int = 0
    spirce: int = 0
    fremen_influence: int = 0


class Location(BaseModel):

    name: str
    agent_icon: AgentIcon
    combat: bool = False
    control: Control | None = None
    cost: Cost = Cost()  # TODO: set cost for the locations that have one.
    free: bool = True

    def pay(self, player_id: int) -> None:
        raise NotImplementedError("This method should be overridden in subclasses")

    def reward(self, player_id: int) -> None:
        raise NotImplementedError("This method should be overridden in subclasses")


class SpiceLocation(Location):

    extra_spice: int = 0

    def produce_spice(self):
        if self.free:
            self.extra_spice += 1

    def pay(self, player_id: int) -> None:
        raise NotImplementedError("This method should be overridden in subclasses")

    def reward(self, player_id: int) -> None:
        raise NotImplementedError("This method should be overridden in subclasses")


class Arrakeen(Location):

    name: str = "arrakeen"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    control: Control | None = SolariControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Carthag(Location):

    name: str = "carthag"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    control: Control | None = SolariControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Conspire(Location):

    name: str = "conspire"
    agent_icon: AgentIcon = AgentIcon.EMPEROR

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class FoldSpace(Location):

    name: str = "fold_space"
    agent_icon: AgentIcon = AgentIcon.SPACING_GUILD

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class TheGreatFlat(SpiceLocation):

    name: str = "the_great_flat"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HaggaBasin(SpiceLocation):

    name: str = "hagga_basin"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        self.extra_spice = 0


class HallOfOratory(Location):

    name: str = "hall_of_oratory"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HardyWarriors(Location):

    name: str = "hardy_warriors"
    agent_icon: AgentIcon = AgentIcon.FREMEN
    combat: bool = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Heighliner(Location):

    name: str = "heighliner"
    agent_icon: AgentIcon = AgentIcon.SPACING_GUILD
    combat: bool = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class HighCouncil(Location):

    name: str = "high_council"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class ImperialBasin(SpiceLocation):

    name: str = "imperial_basin"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True
    control: Control | None = SpiceControl()

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        self.extra_spice = 0


class Mentat(Location):

    name: str = "mentat"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class RallyTroops(Location):

    name: str = "rally_troops"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class ResearchStation(Location):

    name: str = "research_location"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Secrets(Location):

    name: str = "secrets"
    agent_icon: AgentIcon = AgentIcon.BENE_GESSERIT

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SecureContract(Location):

    name: str = "secure_contract"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SelectiveBreeding(Location):

    name: str = "selective_breeding"
    agent_icon: AgentIcon = AgentIcon.BENE_GESSERIT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SellMelange(Location):

    name: str = "sell_melange"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class SietchTabr(Location):

    name: str = "sietch_tabr"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Stillsuits(Location):

    name: str = "stillsuits"
    agent_icon: AgentIcon = AgentIcon.FREMEN
    combat: bool = True

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Swordmaster(Location):

    name: str = "swordmaster"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def pay(self, player_id: int) -> None:
        # TODO
        ...

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Wealth(Location):

    name: str = "wealth"
    agent_icon: AgentIcon = AgentIcon.EMPEROR

    def pay(self, player_id: int) -> None:
        return

    def reward(self, player_id: int) -> None:
        # TODO
        ...


class Locations(BaseModel):

    all_locations: list[Location] = []
    spice_locations: list[SpiceLocation] = []

    def __init__(self, **data) -> None:
        super().__init__(**data)
        self.all_locations = [
            subclass()  # pyright: ignore[reportCallIssue]
            for subclass in Location.__subclasses__()
            if subclass is not SpiceLocation
        ]
        self.spice_locations = [
            subclass()  # pyright: ignore[reportCallIssue]
            for subclass in SpiceLocation.__subclasses__()
        ]
        self.all_locations += self.spice_locations
