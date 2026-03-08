from typing import TYPE_CHECKING, Self

from pydantic import BaseModel, model_validator

from dune_imperium.elements.icons import AgentIcon
from dune_imperium.elements.tokens.agents import Agent
from dune_imperium.utils.utils import all_subclasses, item_name_to_item_class_name

if TYPE_CHECKING:
    from dune_imperium.game import Game
    from dune_imperium.player import Player


class NotEnoughResourcesError(Exception):
    pass


class Cost(BaseModel):

    water: int = 0
    solari: int = 0
    spice: int = 0
    fremen_influence: int = 0


class Location(BaseModel):

    name: str
    agent_icon: AgentIcon
    combat: bool = False
    cost: Cost = Cost()
    free: bool = True
    control_player_id: int | None = None

    def _check_enough_resources(self, player: "Player", game: "Game") -> bool:
        if player.resources.water < self.cost.water:
            return False
        if player.resources.solari < self.cost.solari:
            return False
        if player.resources.spice < self.cost.spice:
            return False
        if game.fremen_influence.influence[player.id] < self.cost.fremen_influence:
            return False
        return True

    def pay(self, player: "Player", game: "Game") -> None:
        if not self._check_enough_resources(player, game):
            raise NotEnoughResourcesError(
                "Not enough resources to deploy an agent to this location"
            )
        player.resources.water -= self.cost.water
        player.resources.solari -= self.cost.solari
        player.resources.spice -= self.cost.spice

    def reward(self, player: "Player", game: "Game") -> None:
        raise NotImplementedError("This method should be overridden in subclasses")

    def control(self, game: "Game") -> None:
        pass


class SpiceLocation(Location):

    extra_spice: int = 0

    def produce_spice(self):
        if self.free:
            self.extra_spice += 1


class Arrakeen(Location):

    name: str = "arrakeen"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    control_player_id: int | None = None

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(1)
        card = player.decks.source_deck.pop()
        player.decks.hand.add(card)
        # TODO: ask player for deployment of troops

    def control(self, game: "Game") -> None:
        if self.control_player_id is not None:
            game.players[self.control_player_id].resources.solari += 1


class Carthag(Location):

    name: str = "carthag"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    control_player_id: int | None = None

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(1)
        intrigue_card = game.intrigue_deck.pop()
        player.decks.intrigues.add(intrigue_card)
        # TODO: ask player for deployment of troops

    def control(self, game: "Game") -> None:
        if self.control_player_id is not None:
            game.players[self.control_player_id].resources.solari += 1


class Conspire(Location):

    name: str = "conspire"
    agent_icon: AgentIcon = AgentIcon.EMPEROR
    cost: Cost = Cost(spice=4)

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(2)
        intrigue_card = game.intrigue_deck.pop()
        player.decks.intrigues.add(intrigue_card)
        player.resources.solari += 5
        game.emperor_influence.increase_influence(player, game)


class FoldSpace(Location):

    name: str = "fold_space"
    agent_icon: AgentIcon = AgentIcon.SPACING_GUILD

    def reward(self, player: "Player", game: "Game") -> None:
        fold_space_card = game.fold_space_deck.pop()
        player.decks.discard_pile.add(fold_space_card)
        game.spacing_guild_influence.increase_influence(player, game)


class TheGreatFlat(SpiceLocation):

    name: str = "the_great_flat"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True
    cost: Cost = Cost(water=2)

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.spice += 3 + self.extra_spice
        self.extra_spice = 0
        # TODO: ask player for deployment of troops


class HaggaBasin(SpiceLocation):

    name: str = "hagga_basin"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True
    cost: Cost = Cost(water=1)

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.spice += 2 + self.extra_spice
        self.extra_spice = 0
        # TODO: ask player for deployment of troops


class HallOfOratory(Location):

    name: str = "hall_of_oratory"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(1)
        # TODO: check how to add 1 to player's persuasion value for the rest of the turn


class HardyWarriors(Location):

    name: str = "hardy_warriors"
    agent_icon: AgentIcon = AgentIcon.FREMEN
    combat: bool = True
    cost: Cost = Cost(water=1)

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(2)
        game.fremen_influence.increase_influence(player, game)
        # TODO: ask player for deployment of troops


class Heighliner(Location):

    name: str = "heighliner"
    agent_icon: AgentIcon = AgentIcon.SPACING_GUILD
    combat: bool = True
    cost: Cost = Cost(spice=6)

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(5)
        player.resources.water += 2
        game.spacing_guild_influence.increase_influence(player, game)
        # TODO: ask player for deployment of troops


class HighCouncil(Location):

    name: str = "high_council"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT
    cost: Cost = Cost(solari=5)

    def reward(self, player: "Player", game: "Game") -> None:
        # TODO: manage council
        ...


class ImperialBasin(SpiceLocation):

    name: str = "imperial_basin"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE
    combat: bool = True
    control_player_id: int | None = None

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.spice += 1 + self.extra_spice
        self.extra_spice = 0
        # TODO: ask player for deployment of troops

    def control(self, game: "Game") -> None:
        if self.control_player_id is not None:
            game.players[self.control_player_id].resources.spice += 1


class Mentat(Location):

    name: str = "mentat"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT
    cost: Cost = Cost(solari=2)

    def reward(self, player: "Player", game: "Game") -> None:
        card = player.decks.source_deck.pop()
        player.decks.hand.add(card)
        # TODO: manage mentat


class RallyTroops(Location):

    name: str = "rally_troops"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT
    cost: Cost = Cost(solari=4)

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(4)


class ResearchStation(Location):

    name: str = "research_station"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    cost: Cost = Cost(water=2)

    def reward(self, player: "Player", game: "Game") -> None:
        for _ in range(3):
            card = player.decks.source_deck.pop()
            player.decks.hand.add(card)
        # TODO: ask player for deployment of troops


class Secrets(Location):

    name: str = "secrets"
    agent_icon: AgentIcon = AgentIcon.BENE_GESSERIT

    def reward(self, player: "Player", game: "Game") -> None:
        intrigue_card = game.intrigue_deck.pop()
        player.decks.intrigues.add(intrigue_card)
        # TODO: ask other players to give you an intrigue card at random if they have more than 3


class SecureContract(Location):

    name: str = "secure_contract"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.solari += 3


class SelectiveBreeding(Location):

    name: str = "selective_breeding"
    agent_icon: AgentIcon = AgentIcon.BENE_GESSERIT
    cost: Cost = Cost(spice=2)

    def reward(self, player: "Player", game: "Game") -> None:
        game.bene_gesserit_influence.increase_influence(player, game)
        # TODO: if player trashes a card it can draw 2
        ...


class SellMelange(Location):

    name: str = "sell_melange"
    agent_icon: AgentIcon = AgentIcon.SPICE_TRADE

    def reward(self, player: "Player", game: "Game") -> None:
        # TODO: ask player how many spice they want to sell and manage the exchange rate
        ...


class SietchTabr(Location):

    name: str = "sietch_tabr"
    agent_icon: AgentIcon = AgentIcon.CITY
    combat: bool = True
    cost: Cost = Cost(fremen_influence=2)

    def reward(self, player: "Player", game: "Game") -> None:
        player.troops.recruit(1)
        player.resources.water += 1
        game.fremen_influence.increase_influence(player, game)
        # TODO: ask player for deployment of troops


class Stillsuits(Location):

    name: str = "stillsuits"
    agent_icon: AgentIcon = AgentIcon.FREMEN
    combat: bool = True

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.water += 1
        game.fremen_influence.increase_influence(player, game)
        # TODO: ask player for deployment of troops


class Swordmaster(Location):

    name: str = "swordmaster"
    agent_icon: AgentIcon = AgentIcon.LANDSRAAT
    cost: Cost = Cost(solari=8)

    def reward(self, player: "Player", game: "Game") -> None:
        player.agents.append(Agent())


class Wealth(Location):

    name: str = "wealth"
    agent_icon: AgentIcon = AgentIcon.EMPEROR

    def reward(self, player: "Player", game: "Game") -> None:
        player.resources.solari += 2
        game.emperor_influence.increase_influence(player, game)


class Locations(BaseModel):

    all_locations_dict: dict[str, Location] = {}
    spice_locations_dict: dict[str, SpiceLocation] = {}

    def initialize(self) -> Self:
        for subclass in all_subclasses(Location):
            if subclass is SpiceLocation:
                continue
            location_name = subclass.model_fields["name"].default
            self.all_locations_dict.update(
                {location_name: subclass()}  # pyright: ignore[reportCallIssue]
            )
            if issubclass(subclass, SpiceLocation):
                self.spice_locations_dict.update(
                    {location_name: subclass()}  # pyright: ignore[reportCallIssue]
                )
        return self

    @model_validator(mode="before")
    def resolve_location_classes(cls, values):
        all_locations_dict = {}
        spice_locations_dict = {}
        for location_name, location_values in values.get(
            "all_locations_dict", {}
        ).items():
            location_class_name = item_name_to_item_class_name(location_name)
            for subclass in all_subclasses(Location):
                if subclass.__name__ == location_class_name:
                    all_locations_dict[location_name] = subclass(**location_values)
                    if issubclass(subclass, SpiceLocation):
                        spice_locations_dict[location_name] = subclass(
                            **location_values
                        )
                    break
            else:
                raise ValueError(
                    f"Location class not found for location: {location_name}"
                )

        return {
            "all_locations_dict": all_locations_dict,
            "spice_locations_dict": spice_locations_dict,
        }

    @property
    def all_locations(self) -> list[Location]:
        return list(self.all_locations_dict.values())

    @property
    def spice_locations(self) -> list[SpiceLocation]:
        return list(self.spice_locations_dict.values())
