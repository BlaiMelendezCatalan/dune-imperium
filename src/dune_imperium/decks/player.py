from random import shuffle
from pydantic import BaseModel
from typing import cast

from dune_imperium.decks.base import BaseBigCard
from dune_imperium.decks.initial import InitialDeck
from dune_imperium.decks.intrigue import IntrigueCard


class Deck(BaseModel):

    cards: list[BaseBigCard] = []

    def __init__(self, **data) -> None:
        super().__init__(**data)
        initial_deck = InitialDeck()
        self.cards = cast(list[BaseBigCard], initial_deck.get_cards())

    def rebuild(self, cards: list[BaseBigCard]) -> None:
        shuffle(cards)
        self.cards = cards


class PlayerDeck(BaseModel):

    card_dict: dict[str, BaseBigCard] = {}

    def add(self, card: BaseBigCard) -> None:
        self.card_dict.update({card.name: card})

    def pop(self, card_name: str) -> BaseBigCard:
        return self.card_dict.pop(card_name)

    @property
    def cards(self) -> list[BaseBigCard]:
        return list(self.card_dict.values())


class Hand(PlayerDeck): ...


class InPlay(PlayerDeck): ...


class DiscardPile(PlayerDeck): ...


class PlayerIntrigueDeck(BaseModel):

    intrigue_dict: dict[str, IntrigueCard] = {}

    def add(self, card: IntrigueCard) -> None:
        self.intrigue_dict.update({card.name: card})

    def pop(self, card_name: str) -> IntrigueCard:
        return self.intrigue_dict.pop(card_name)

    @property
    def intrigues(self) -> list[IntrigueCard]:
        return list(self.intrigue_dict.values())


class Intrigues(PlayerIntrigueDeck): ...
