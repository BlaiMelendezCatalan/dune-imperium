from typing import TYPE_CHECKING, Self

from dune_imperium.decks.base import BaseBigCard, BaseSourceDeck
from dune_imperium.elements.icons import AgentIcon

if TYPE_CHECKING:
    from dune_imperium.player import Player


class InitialCard(BaseBigCard): ...


class ConvincingArgument(InitialCard):

    name: str = "convincing_argument"
    repetitions: int = 2

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class Dagger(InitialCard):

    name: str = "dagger"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]

    def revelation_reward(self, player: "Player") -> None:
        player.swords += 1


class Diplomacy(InitialCard):

    name: str = "diplomacy"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class DuneTheDesertPlanet(InitialCard):

    name: str = "dune_the_desert_planet"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class Reconnaissance(InitialCard):

    name: str = "reconnaissance"
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class SignetRing(InitialCard):

    name: str = "signet_ring"
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


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
