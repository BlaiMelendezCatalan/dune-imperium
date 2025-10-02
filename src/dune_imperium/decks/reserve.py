from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.factions import Faction
from dune_imperium.agent_icons.icons import AgentIcon


class ReserveCard(BaseBigCard): ...


class ArrakisLiaison(ReserveCard):

    name: str = "arrakis_liaison"
    repetitions: int = 8
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]


class FoldSpace(ReserveCard):

    name: str = "foldspace"
    repetitions: int = 6
    persuasion_cost: int = 0
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]


class TheSpiceMustFlow(ReserveCard):

    name: str = "the_spice_must_flow"
    repetitions: int = 10
    persuasion_cost: int = 9
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]


class ArrakisLiaisonDeck(BaseDeck[ArrakisLiaison]):

    def __init__(self, **data) -> None:
        super().__init__(ArrakisLiaison, shuffle_deck=False, **data)


class FoldSpaceDeck(BaseDeck[FoldSpace]):

    def __init__(self, **data) -> None:
        super().__init__(FoldSpace, shuffle_deck=False, **data)


class TheSpiceMustFlowDeck(BaseDeck[TheSpiceMustFlow]):

    def __init__(self, **data) -> None:
        super().__init__(TheSpiceMustFlow, shuffle_deck=False, **data)
