from typing import Self

from pydantic import BaseModel, model_validator

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.map.control import Control, SolariControl, SpiceControl
from dune_imperium.utils.utils import all_subclasses, item_name_to_item_class_name


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

    all_locations_dict: dict[str, Location] = {}
    spice_locations_dict: dict[str, SpiceLocation] = {}

    def initialize(self) -> Self:
        for subclass in all_subclasses(Location):
            if subclass is SpiceLocation:
                continue
            self.all_locations_dict.update(
                {subclass.__name__: subclass()}  # pyright: ignore[reportCallIssue]
            )
            if issubclass(subclass, SpiceLocation):
                self.spice_locations_dict.update(
                    {subclass.__name__: subclass()}  # pyright: ignore[reportCallIssue]
                )
        return self

    @model_validator(mode="before")
    def resolve_location_classes(cls, values):
        all_locations_dict = {}
        spice_locations_dict = {}
        for location_name, location_values in values.get("all_locations", {}):
            location_class_name = item_name_to_item_class_name(location_name)
            for subclass in all_subclasses(Location):
                if subclass.__name__ == location_class_name:
                    all_locations_dict[subclass.__name__] = subclass(**location_values)
                    if issubclass(subclass, SpiceLocation):
                        spice_locations_dict[subclass.__name__] = subclass(
                            **location_values
                        )
                    break
            else:
                raise ValueError(
                    f"Card class not found for card name: {values.get('name')}"
                )

        return {
            "all_locations": all_locations_dict,
            "spice_locations": spice_locations_dict,
        }

    @property
    def all_locations(self) -> list[Location]:
        return list(self.all_locations_dict.values())

    @property
    def spice_locations(self) -> list[SpiceLocation]:
        return list(self.spice_locations_dict.values())
