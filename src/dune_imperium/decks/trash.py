from typing import Generic, TypeVar

from pydantic import BaseModel

from dune_imperium.decks.base import BaseBigCard, BaseCard
from dune_imperium.decks.conflicts import ConflictCard
from dune_imperium.decks.intrigue import IntrigueCard


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseTrashDeck(BaseModel, Generic[T_Card]):

    cards: list[T_Card] = []

    def __init__(self, **data) -> None:
        super().__init__(**data)

    def add(self, cards: list[T_Card]) -> None:
        self.cards.extend(cards)


class TrashedIntrigueDeck(BaseTrashDeck[IntrigueCard]): ...


class TrashedBigCardDeck(BaseTrashDeck[BaseBigCard]): ...


class TrashedConflictDeck(BaseModel):

    cards: list[ConflictCard] = []

    def add(self, card: ConflictCard) -> None:
        self._validate_card(card)
        self.cards.append(card)

    def _validate_card(self, card: ConflictCard) -> None:
        if card in self.cards:
            raise ValueError(f"Card {card.name} is already in the trash deck.")
        if not isinstance(card, ConflictCard):
            raise ValueError(f"Card {card.name} is not of type ConflictCard.")
