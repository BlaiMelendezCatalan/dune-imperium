from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.agent_icons.icons import AgentIcon


class ConvincingArgument(BaseBigCard):

    name: str = "convincing_argument"
    repetitions: int = 2


class Dagger(BaseBigCard):

    name: str = "dagger"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]


class Diplomacy(BaseBigCard):

    name: str = "diplomacy"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]


class DuneTheDesertPlanet(BaseBigCard):

    name: str = "dune_the_desert_planet"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]


class Reconnaissance(BaseBigCard):

    name: str = "reconnaissance"
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class SignetRing(BaseBigCard):

    name: str = "signet_ring"
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]


class SeekAllies(BaseBigCard):

    name: str = "seek_allies"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]


class InitialDeck(BaseDeck[BaseBigCard]):

    def __init__(self, **data) -> None:
        super().__init__(BaseBigCard, shuffle_deck=True, **data)
