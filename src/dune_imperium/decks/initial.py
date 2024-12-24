from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.card_states import CardState
from dune_imperium.icons import AgentIcon


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

    name = "convincing_argument"
    repetitions = 2

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Dagger(InitialCard):

    name = "dagger"
    repetitions = 2
    agent_icons = [AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Diplomacy(InitialCard):

    name = "diplomacy"
    agent_icons = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DuneTheDesertPlanet(InitialCard):

    name = "dune_the_desert_planet"
    repetitions = 2
    agent_icons = [AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Reconnaissance(InitialCard):

    name = "reconnaissance"
    agent_icons = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SignetRing(InitialCard):

    name = "signet_ring"
    agent_icons = [AgentIcon.LANDSRAAT, AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SeekAllies(InitialCard):

    name = "seek_allies"
    agent_icons = [
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
