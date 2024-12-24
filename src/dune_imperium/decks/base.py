from abc import ABC, abstractmethod
from random import shuffle
from typing import Generic, TypeVar
from pydantic import BaseModel

from dune_imperium.decks.card_states import CardState
from dune_imperium.icons import AgentIcon


class BaseCard(BaseModel):

    name: str
    repetitions: int = 1
    state: CardState


class BaseBigCard(BaseCard, ABC):

    agent_icons: list[AgentIcon] = []

    @abstractmethod
    def play_as_agent(self, player_id: int) -> None:
        """Apply agent logic and let the user decide the location of the agent."""  # TODO fix docstring
        pass

    @abstractmethod
    def play_as_revelation(self, player_id: int) -> None:
        """Apply revelation logic"""  # TODO fix docstring
        pass

    @abstractmethod
    def trash(self) -> None:
        """Trash card"""
        pass


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseDeck(BaseModel, Generic[T_Card]):

    _cards: dict[str, T_Card]

    def __init__(self, card_class: type[T_Card], shuffle_deck: bool, **data) -> None:
        super().__init__(**data)
        cards: list[card_class] = []
        for (
            subclass
        ) in card_class.__subclasses__():  # pyright: ignore[reportAttributeAccessIssue]
            repetitions: int = subclass.model_fields["repetitions"].default
            for i in range(repetitions):
                card = subclass()  # pyright: ignore[reportCallIssue]
                self.add_repetition_to_card_name(card, i)
                cards.append(card)
        if shuffle_deck:
            shuffle(cards)
        self._cards = {card.name: card for card in cards}

    @property
    def cards(self) -> dict[str, T_Card]:
        return self._cards

    @staticmethod
    def add_repetition_to_card_name(card: BaseCard, repetition: int):
        card.name += f"__{repetition}"
