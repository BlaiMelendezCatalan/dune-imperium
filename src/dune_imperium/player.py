from pydantic import BaseModel

from dune_imperium.decks.leaders import Leader
from dune_imperium.decks.player import (
    DiscardPile,
    Hand,
    InPlay,
    Intrigues,
    PlayerSourceDeck,
)
from dune_imperium.elements.tokens.agents import Agent
from dune_imperium.elements.tokens.resources import Resources
from dune_imperium.elements.tokens.troops import TroopPool


class Player(BaseModel):

    id: int

    leader: Leader

    resources: Resources = Resources()

    persuasion: int = 0
    swords: int = 0

    agents: list[Agent] = [Agent() for _ in range(2)]

    troops: TroopPool = TroopPool()

    source_deck: PlayerSourceDeck = PlayerSourceDeck().initialize()
    hand: Hand = Hand()
    in_play: InPlay = InPlay()
    discard_pile: DiscardPile = DiscardPile()
    intrigues: Intrigues = Intrigues()
