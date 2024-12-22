from abc import ABC, abstractmethod
from random import shuffle

from dune_imperium.factions import Faction, Factions
from dune_imperium.icons import AgentIcon, AgentIcons


class ReserveCard(ABC):

    name: str
    repetitions: int
    factions: Factions = Factions()
    cost: int
    agent_icons: AgentIcons = AgentIcons()

    def acquire(self, player_id: int) -> None:
        # TODO remove from imperium deck and place in player's discard deck. Apply any necessary logic
        ...

    @abstractmethod
    def play_as_agent(self, player_id: int) -> None:
        # TODO apply logic and let the user decide the location of the agent.
        pass

    @abstractmethod
    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass


class ArrakisLiaison(ReserveCard):

    name = "arrakis_liaison"
    repetitions = 8
    factions = Factions(Faction.FREMEN)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FoldSpace(ReserveCard):

    name = "foldspace"
    repetitions = 6
    cost = 0
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY)

    def acquire(self, player_id: int) -> None:
        # TODO Add special extra logic
        ...

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TheSpiceMustFlow(ReserveCard):

    name = "the_spice_must_flow"
    repetitions = 10
    cost = 9
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY)

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ReserveDeck:

    cards: list[ReserveCard]

    def initialize(self):
        self.cards = [
            subclass()
            for subclass in ReserveCard.__subclasses__()
            for _ in range(subclass.repetitions)
        ]
        shuffle(self.cards)
