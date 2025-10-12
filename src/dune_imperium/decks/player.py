from random import shuffle
from pydantic import BaseModel
from typing import Self, cast

from dune_imperium.decks.base import BaseBigCard
from dune_imperium.decks.initial import InitialDeck
from dune_imperium.decks.intrigue import IntrigueCard


class SourceDeck(BaseModel):

    cards: list[BaseBigCard] = []

    def initialize(self) -> Self:
        initial_deck = InitialDeck().initialize()
        self.cards = cast(list[BaseBigCard], initial_deck.cards)
        return self

    def rebuild(self, cards: list[BaseBigCard]) -> None:
        shuffle(cards)
        self.cards = cards

    def pop(self) -> BaseBigCard:
        return self.cards.pop()


class PlayerDeck(BaseModel):

    card_dict: dict[str, BaseBigCard] = {}

    def add(self, card: BaseBigCard) -> None:
        self.card_dict.update({card.name: card})

    def pop(self, card_name: str | None = None) -> BaseBigCard:
        if card_name is None:
            card = self.cards.pop()
            self.card_dict.pop(card.name)
            return card
        return self.card_dict.pop(card_name)

    @property
    def cards(self) -> list[BaseBigCard]:
        return list(self.card_dict.values())


class Hand(PlayerDeck): ...


class InPlay(PlayerDeck): ...


class DiscardPile(PlayerDeck): ...


class Intrigues(BaseModel):

    intrigue_dict: dict[str, IntrigueCard] = {}

    def add(self, card: IntrigueCard) -> None:
        self.intrigue_dict.update({card.name: card})

    def pop(self, card_name: str) -> IntrigueCard:
        return self.intrigue_dict.pop(card_name)

    @property
    def intrigues(self) -> list[IntrigueCard]:
        return list(self.intrigue_dict.values())
