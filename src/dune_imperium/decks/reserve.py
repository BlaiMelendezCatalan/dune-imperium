from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.card_states import CardState
from dune_imperium.factions import Faction
from dune_imperium.icons import AgentIcon


class ReserveCard(BaseBigCard):

    factions: list[Faction] = []
    cost: int
    state: CardState = CardState.IN_DECK

    def acquire(self, player_id: int) -> None:
        # TODO remove from imperium deck and place in player's discard deck. Apply any necessary logic
        ...

    def play_as_agent(self, player_id: int) -> None:
        # TODO apply logic and let the user decide the location of the agent.
        pass

    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass

    def trash(self):
        # TODO
        pass


class ArrakisLiaison(ReserveCard):

    name = "arrakis_liaison"
    repetitions = 8
    factions = [Faction.FREMEN]
    cost = 2
    agent_icons = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FoldSpace(ReserveCard):

    name = "foldspace"
    repetitions = 6
    cost = 0
    agent_icons = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def acquire(self, player_id: int) -> None:
        # TODO Add special extra logic
        ...

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TheSpiceMustFlow(ReserveCard):

    name = "the_spice_must_flow"
    repetitions = 10
    cost = 9
    agent_icons = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ArrakisLiaisonDeck(BaseDeck[ArrakisLiaison]):

    def __init__(self, **data) -> None:
        super().__init__(ArrakisLiaison, shuffle_deck=False, **data)


class FoldSpaceDeck(BaseDeck[FoldSpace]):

    def __init__(self, **data) -> None:
        super().__init__(FoldSpace, shuffle_deck=False, **data)


class TheSpiceMustFlowDeck(BaseDeck[TheSpiceMustFlow]):

    def __init__(self, **data) -> None:
        super().__init__(TheSpiceMustFlow, shuffle_deck=False, **data)
