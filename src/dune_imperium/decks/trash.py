from typing import Generic, TypeVar

from pydantic import BaseModel

from dune_imperium.decks.base import BaseBigCard, BaseCard
from dune_imperium.decks.conflicts import ConflictCard
from dune_imperium.decks.intrigue import IntrigueCard


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseTrashDeck(BaseModel, Generic[T_Card]):

    _cards: list[T_Card] = []
    _card_class: type[T_Card]

    def __init__(self, card_class: type[T_Card], **data) -> None:
        super().__init__(**data)
        self._card_class = card_class

    def add(self, cards: list[T_Card]) -> None:
        self._validate_card(cards)
        self._cards.extend(cards)

    def _validate_card(self, cards: list[T_Card]) -> None:
        for card in cards:
            if card in self._cards:
                raise ValueError(f"Card {card.name} is already in the trash deck.")
            if not isinstance(card, self._card_class):
                raise ValueError(f"Card {card.name} is not of type {self._card_class}.")

    @property
    def cards(self) -> list[T_Card]:
        return self._cards


class TrashedIntrigueDeck(BaseTrashDeck[IntrigueCard]):

    def __init__(self, **data) -> None:
        super().__init__(IntrigueCard, **data)


class TrashedBigCardDeck(BaseTrashDeck[BaseBigCard]):

    def __init__(self, **data) -> None:
        super().__init__(BaseBigCard, **data)


class TrashedConflictDeck(BaseModel):

    _cards: list[ConflictCard] = []

    def add(self, card: ConflictCard) -> None:
        self._validate_card(card)
        self._cards.append(card)

    def _validate_card(self, card: ConflictCard) -> None:
        if card in self._cards:
            raise ValueError(f"Card {card.name} is already in the trash deck.")
        if not isinstance(card, ConflictCard):
            raise ValueError(f"Card {card.name} is not of type ConflictCard.")

    @property
    def cards(self) -> list[ConflictCard]:
        return self._cards
