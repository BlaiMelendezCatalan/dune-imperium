from random import shuffle
from typing import Self, TypeVar, cast

from dune_imperium.decks.base import BaseBigCard, BaseOpenDeck, BaseSourceDeck
from dune_imperium.decks.initial import InitialDeck

T_BigCard = TypeVar("T_BigCard", bound=BaseBigCard)


class PlayerSourceDeck(BaseSourceDeck):

    def initialize(self) -> Self:
        initial_deck = InitialDeck().initialize()
        self.cards = cast(list[BaseBigCard], initial_deck.cards)
        return self

    def rebuild(self, cards: list[T_BigCard]) -> None:
        shuffle(cards)
        self.cards = cards


class Hand(BaseOpenDeck): ...


class InPlay(BaseOpenDeck): ...


class DiscardPile(BaseOpenDeck): ...


class Intrigues(BaseOpenDeck): ...
