from typing import TYPE_CHECKING, Self
from dune_imperium.decks.base import BaseBigCard, BaseSourceDeck
from dune_imperium.agent_icons.icons import AgentIcon

if TYPE_CHECKING:
    from dune_imperium.player import Player


class InitialCard(BaseBigCard): ...


class ConvincingArgument(InitialCard):

    name: str = "convincing_argument"
    repetitions: int = 2

    def revelation_reward(self, player: "Player") -> None:
        print(f"****{player.persuasion=}****")
        player.persuasion += 1
        print(f"****{player.persuasion=}****")


class Dagger(InitialCard):

    name: str = "dagger"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]


class Diplomacy(InitialCard):

    name: str = "diplomacy"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]


class DuneTheDesertPlanet(InitialCard):

    name: str = "dune_the_desert_planet"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]


class Reconnaissance(InitialCard):

    name: str = "reconnaissance"
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class SignetRing(InitialCard):

    name: str = "signet_ring"
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]


class SeekAllies(InitialCard):

    name: str = "seek_allies"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]


class InitialDeck(BaseSourceDeck[InitialCard]):

    def initialize(self) -> Self:
        super()._initialize(InitialCard)
        return self
