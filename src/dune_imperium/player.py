from pydantic import BaseModel

from dune_imperium.decks.player import DiscardPile, InPlay, Intrigues, SourceDeck, Hand
from dune_imperium.decks.leaders import Leader
from dune_imperium.map.trackers import InfluenceTracker
from dune_imperium.tokens.agents import Agent
from dune_imperium.tokens.resources import Resources
from dune_imperium.tokens.troops import Troop


class Player(BaseModel):

    id: int

    leader: Leader

    victory_points: int

    resources: Resources = Resources()

    persuasion: int = 0
    swords: int = 0

    agents: list[Agent] = [Agent() for _ in range(2)]

    troops: list[Troop] = [Troop() for _ in range(16)]

    fremen_influence: InfluenceTracker = InfluenceTracker()
    bene_gesserit_influence: InfluenceTracker = InfluenceTracker()
    spacing_guild_influence: InfluenceTracker = InfluenceTracker()
    emperor_influence: InfluenceTracker = InfluenceTracker()

    source_deck: SourceDeck = SourceDeck()
    hand: Hand = Hand()
    in_play: InPlay = InPlay()
    discard_pile: DiscardPile = DiscardPile()
    intrigues: Intrigues = Intrigues()
