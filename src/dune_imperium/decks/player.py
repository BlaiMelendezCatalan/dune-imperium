from random import shuffle
from typing import Self, TypeVar, cast

from pydantic import BaseModel

from dune_imperium.decks.base import BaseBigCard, BaseOpenDeck, BaseSourceDeck
from dune_imperium.decks.initial import InitialDeck

T_BigCard = TypeVar("T_BigCard", bound=BaseBigCard)


class PlayerSourceDeck(BaseSourceDeck):

    def initialize(self) -> Self:
        initial_deck = InitialDeck().initialize()
        self.cards = cast(list[BaseBigCard], initial_deck.cards)
        return self


class Hand(BaseOpenDeck): ...


class InPlay(BaseOpenDeck): ...


class DiscardPile(BaseOpenDeck): ...


class Intrigues(BaseOpenDeck): ...


class PlayerDecks(BaseModel):

    source_deck: PlayerSourceDeck = PlayerSourceDeck().initialize()
    hand: Hand = Hand()
    in_play: InPlay = InPlay()
    discard_pile: DiscardPile = DiscardPile()
    intrigues: Intrigues = Intrigues()

    def rebuild_source_deck(self) -> None:
        shuffle(self.discard_pile.cards)
        self.source_deck.cards = self.discard_pile.cards
        self.discard_pile.card_dict = {}

    def draw(self, number: int) -> list[BaseBigCard]:
        drawn_cards = self.cards[-number:]
        if len(drawn_cards) < number:
            self.rebuild_source_deck()
        self.cards = self.cards[:-number]
        return drawn_cards
