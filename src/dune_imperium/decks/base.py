from random import shuffle
from typing import TYPE_CHECKING, Generic, TypeVar
from pydantic import BaseModel

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.decks.factions import Faction

if TYPE_CHECKING:
    from dune_imperium.player import Player


class BaseCard(BaseModel):

    name: str
    repetitions: int = 1


class BaseBigCard(BaseCard):

    agent_icons: list[AgentIcon] = []
    factions: list[Faction] = []
    persuasion_cost: int = 0

    def agent_reward(self, player: "Player") -> None:
        pass

    def revelation_reward(self, player: "Player") -> None:
        print("********")


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseDeck(BaseModel, Generic[T_Card]):

    cards: list[T_Card] = []

    def _initialize(self, card_class: type[T_Card]) -> None:
        for (
            subclass
        ) in card_class.__subclasses__():  # pyright: ignore[reportAttributeAccessIssue]
            print(f"Adding {subclass.__name__}")
            repetitions: int = subclass.model_fields["repetitions"].default
            for i in range(repetitions):
                card = subclass()  # pyright: ignore[reportCallIssue]
                self._add_repetition_to_card_name(card, i)
                self.cards.append(card)
        shuffle(self.cards)

    @staticmethod
    def _add_repetition_to_card_name(card: BaseCard, repetition: int):
        card.name += f"__{repetition}"

    def pop(self) -> T_Card:
        return self.cards.pop()

    def add(self, cards: list[T_Card]) -> None:
        self.cards.extend(cards)
