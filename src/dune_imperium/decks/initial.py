from abc import ABC, abstractmethod
from random import shuffle

from dune_imperium.icons import AgentIcon, AgentIcons


class InitialCard(ABC):

    name: str
    repetitions: int = 1
    agent_icons: AgentIcons = AgentIcons()

    @abstractmethod
    def play_as_agent(self, player_id: int) -> None:
        # TODO apply logic and let the user decide the location of the agent.
        pass

    @abstractmethod
    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass


class ConvincingArgument(InitialCard):

    name = "convincing_argument"
    repetitions = 2

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Dagger(InitialCard):

    name = "dagger"
    repetitions = 2
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Diplomacy(InitialCard):

    name = "diplomacy"
    agent_icons = AgentIcons(
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    )

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DuneTheDesertPlanet(InitialCard):

    name = "dune_the_desert_planet"
    repetitions = 2
    agent_icons = AgentIcons(AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Reconnaissance(InitialCard):

    name = "reconnaissance"
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SignetRing(InitialCard):

    name = "signet_ring"
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SeekAllies(InitialCard):

    name = "seek_allies"
    agent_icons = AgentIcons(
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    )

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class InitialDeck:

    cards: list[InitialCard]

    def initialize(self):
        self.cards = [
            subclass()
            for subclass in InitialCard.__subclasses__()
            for _ in range(subclass.repetitions)
        ]
        shuffle(self.cards)
