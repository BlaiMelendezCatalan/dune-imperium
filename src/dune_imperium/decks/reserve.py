from typing import Self
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

    def initialize(self) -> Self:
        super()._initialize(ArrakisLiaison)
        return self


class FoldSpaceDeck(BaseDeck[FoldSpace]):

    def initialize(self) -> Self:
        super()._initialize(FoldSpace)
        return self


class TheSpiceMustFlowDeck(BaseDeck[TheSpiceMustFlow]):

    def initialize(self) -> Self:
        super()._initialize(TheSpiceMustFlow)
        return self
