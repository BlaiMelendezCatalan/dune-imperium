from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.card_states import CardState
from dune_imperium.agent_icons.icons import AgentIcon


class InitialCard(BaseBigCard):

    state: CardState = CardState.ACQUIRED

    def play_as_agent(self, player_id: int) -> None:
        # TODO apply logic and let the user decide the location of the agent.
        pass

    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass

    def trash(self):
        # TODO
        pass


class ConvincingArgument(InitialCard):

    name: str = "convincing_argument"
    repetitions: int = 2

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Dagger(InitialCard):

    name: str = "dagger"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Diplomacy(InitialCard):

    name: str = "diplomacy"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DuneTheDesertPlanet(InitialCard):

    name: str = "dune_the_desert_planet"
    repetitions: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Reconnaissance(InitialCard):

    name: str = "reconnaissance"
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SignetRing(InitialCard):

    name: str = "signet_ring"
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SeekAllies(InitialCard):

    name: str = "seek_allies"
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class InitialDeck(BaseDeck[InitialCard]):

    def __init__(self, **data) -> None:
        super().__init__(InitialCard, shuffle_deck=True, **data)
