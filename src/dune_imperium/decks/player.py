from random import shuffle
from pydantic import BaseModel
from typing import Generic, Self, TypeVar, cast

from dune_imperium.decks.base import BaseBigCard, BasePlayerDeck
from dune_imperium.decks.initial import InitialDeck


T_BigCard = TypeVar("T_BigCard", bound=BaseBigCard)


class PlayerSourceDeck(BaseModel, Generic[T_BigCard]):

    cards: list[T_BigCard] = []

    def initialize(self) -> Self:
        initial_deck = InitialDeck().initialize()
        self.cards = cast(list[T_BigCard], initial_deck.cards)
        return self

    def rebuild(self, cards: list[T_BigCard]) -> None:
        shuffle(cards)
        self.cards = cards

    def pop(self) -> T_BigCard:
        return self.cards.pop()


class Hand(BasePlayerDeck): ...


class InPlay(BasePlayerDeck): ...


class DiscardPile(BasePlayerDeck): ...


class Intrigues(BasePlayerDeck): ...
