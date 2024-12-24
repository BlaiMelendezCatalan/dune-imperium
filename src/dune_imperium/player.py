from pydantic import BaseModel

from dune_imperium.decks.player import DiscardPile, PlayerDeck, Hand
from dune_imperium.decks.leaders import Leader
from dune_imperium.map.trackers import InfluenceTracker
from dune_imperium.tokens.agents import Agent
from dune_imperium.tokens.troops import Troop
from dune_imperium.tokens.resources import Resources


class Player(BaseModel):

    id: int

    leader: Leader

    first_player: bool

    victory_points: int

    resources: dict[Resources, int] = {
        Resources.WATER: 1,
        Resources.SOLARI: 0,
        Resources.SPICE: 0,
    }

    agents: list[Agent] = [Agent() for _ in range(2)]

    troops: list[Troop] = [Troop() for _ in range(16)]

    fremen_influence: InfluenceTracker = InfluenceTracker()
    bene_gesserit_influence: InfluenceTracker = InfluenceTracker()
    spacing_guild_influence: InfluenceTracker = InfluenceTracker()
    emperor_influence: InfluenceTracker = InfluenceTracker()

    deck: PlayerDeck = PlayerDeck()
    hand: Hand = Hand()
    discard_pile: DiscardPile = DiscardPile()

    @property
    def water(self) -> int:
        return self.resources[Resources.WATER]

    @water.setter
    def water(self, value: int) -> None:
        self.resources[Resources.WATER] = value

    @property
    def solari(self) -> int:
        return self.resources[Resources.SOLARI]

    @solari.setter
    def solari(self, value: int) -> None:
        self.resources[Resources.SOLARI] = value

    @property
    def spice(self) -> int:
        return self.resources[Resources.SPICE]

    @spice.setter
    def spice(self, value: int) -> None:
        self.resources[Resources.SPICE] = value

    def play_card_as_agent(self, card_name):
        if all([agent.deployed for agent in self.agents]):
            return  # TODO this should trigger a pop-up saying there are no more agents to deploy
        self.hand.cards[card_name].play_as_agent(self.id)

    def reveal(self):
        self.hand.reveal(self.id)
