from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.agent_icons.icons import AgentIcon


class InitialCard(BaseBigCard): ...


class ConvincingArgument(InitialCard):

    name: str = "convincing_argument"
    repetitions: int = 2


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


class InitialDeck(BaseDeck[InitialCard]):

    def __init__(self, **data) -> None:
        super().__init__(InitialCard, shuffle_deck=True, **data)
