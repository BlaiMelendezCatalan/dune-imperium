from random import shuffle
from typing import TYPE_CHECKING, Generic, TypeVar

from pydantic import BaseModel, model_validator

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.factions.factions import Faction
from dune_imperium.utils.utils import all_subclasses, item_name_to_item_class_name

if TYPE_CHECKING:
    from dune_imperium.player import Player


class BaseCard(BaseModel):

    name: str
    repetitions: int = 1

    @model_validator(mode="before")
    def resolve_card_class(cls, values):  # TODO blai: is this necessary?
        card_class_name = item_name_to_item_class_name(values.get("name", ""))
        # During initialization, cls is the correct subclass
        if cls.__name__ == card_class_name:
            return values
        for subclass in all_subclasses(BaseCard):
            if subclass.__name__ == card_class_name:
                model_fields = {
                    key: field.default for key, field in subclass.model_fields.items()
                }
                return model_fields

        raise ValueError(f"Card class not found for card name: {values.get('name')}")


class BaseBigCard(BaseCard):

    agent_icons: list[AgentIcon] = []
    factions: list[Faction] = []
    persuasion_cost: int = 0

    def agent_reward(self, player: "Player") -> None:
        raise NotImplementedError("This method should be overridden in subclasses")

    def revelation_reward(self, player: "Player") -> None:
        raise NotImplementedError("This method should be overridden in subclasses")


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseSourceDeck(BaseModel, Generic[T_Card]):

    cards: list[T_Card] = []

    def _initialize(self, card_class: type[T_Card]) -> None:
        for subclass in card_class.__subclasses__():
            repetitions: int = subclass.model_fields["repetitions"].default
            for i in range(repetitions):
                model_fields = {
                    key: field.default for key, field in subclass.model_fields.items()
                }
                card = subclass(**model_fields)
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

    @model_validator(mode="before")
    def resolve_card_classes(cls, values):
        cards = []
        for card in values.get("cards", []):
            card_class_name = item_name_to_item_class_name(card.get("name", ""))
            for subclass in all_subclasses(BaseCard):
                if subclass.__name__ == card_class_name:
                    cards.append(subclass(**card))
                    break
            else:
                raise ValueError(
                    f"Card class not found for card name: {values.get('name')}"
                )

        return {"cards": cards}


class BasePlayerDeck(BaseModel, Generic[T_Card]):

    card_dict: dict[str, T_Card] = {}

    def add(self, card: T_Card) -> None:
        self.card_dict.update({card.name: card})

    def pop(self, card_name: str | None = None) -> T_Card:
        # card_name is None during revelation turn
        if card_name is None:
            card = self.cards.pop()
            self.card_dict.pop(card.name)
            return card
        return self.card_dict.pop(card_name)

    @property
    def cards(self) -> list[T_Card]:
        return list(self.card_dict.values())

    @model_validator(mode="before")
    def resolve_card_classes(cls, values):
        card_dict = {}
        for card_name, card_values in values.get("card_dict", {}).items():
            card_class_name = item_name_to_item_class_name(card_name)
            for subclass in all_subclasses(BaseCard):
                if subclass.__name__ == card_class_name:
                    card_dict[card_name] = subclass(**card_values)
                    break
            else:
                raise ValueError(
                    f"Card class not found for card name: {values.get('name')}"
                )

        return {"card_dict": card_dict}
