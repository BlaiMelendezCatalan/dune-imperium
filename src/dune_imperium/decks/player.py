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
        self.cards = cast(list[BaseBigCard], initial_deck.cards)

    def rebuild(self, cards: list[BaseBigCard]) -> None:
        shuffle(cards)
        self.cards = cards


class Hand(BaseModel):

    cards: dict[str, BaseBigCard] = {}

    def draw(self, *cards: BaseBigCard) -> None:
        self._cards = {card.name: card for card in cards}

    def play_as_agent(self, card_name: str, player_id: int) -> None:
        self._cards[card_name].agent_reward(player_id)

    def reveal(self, player_id: int) -> None:
        [card.revelation_reward(player_id) for card in self._cards.values()]

    def trash(self, card_name: str) -> None:
        self._cards[card_name].trash()


class InPlay(BaseModel):

    cards: dict[str, BaseBigCard] = {}

    def add(self, card: BaseBigCard):
        # TODO
        ...

    def discard(self) -> None:
        # TODO
        ...

    def trash(self) -> None:
        # TODO
        ...


class DiscardPile(BaseModel):

    cards: dict[str, BaseBigCard] = {}

    def add(self, card: BaseBigCard):
        # TODO
        ...

    def trash(self, card: BaseBigCard) -> None:
        # TODO
        ...


class Intrigues(BaseModel):

    cards: dict[str, IntrigueCard] = {}

    def add(self, card: BaseBigCard):
        # TODO
        ...
