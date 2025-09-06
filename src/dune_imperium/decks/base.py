from random import shuffle
from typing import Generic, TypeVar
import httpx
from pydantic import BaseModel

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.decks.factions import Faction


class BaseCard(BaseModel):

    name: str
    repetitions: int = 1


class BaseBigCard(BaseCard):

    agent_icons: list[AgentIcon] = []
    factions: list[Faction] = []
    persuasion_cost: int = 0

    def expose(self): ...

    def acquire(self, player_id: int) -> None:
        url = f"/cards/{"game_name"}/acquire"  # TODO API URL and game_name missing
        payload = {
            "player_id": player_id,
            "card_name": self.name,
        }

        with httpx.Client() as client:
            client.post(url, json=payload)
            # TODO check response?

    def trash(self) -> None: ...

    def icon_click(self, clicked_icon: AgentIcon) -> None:
        # TODO show available locations for this icon
        ...

    def agent_reward(self, player_id: int) -> None:
        # TODO Call agent logic endpoint and let the user decide the location of the agent.
        url = f"/cards/{"game_name"}/{self.name}/agent_reward"  # TODO API URL and game_name missing
        with httpx.Client() as client:
            client.post(url, json={"player_id": player_id})
            # TODO check response in case of no free agents, ...

    def revelation_reward(self, player_id: int) -> None:
        url = f"/cards/{"game_name"}/{self.name}/revelation_reward"  # TODO API URL and game_name missing
        with httpx.Client() as client:
            client.post(url, json={"player_id": player_id})
            # TODO check response?


T_Card = TypeVar("T_Card", bound=BaseCard)


class BaseDeck(BaseModel, Generic[T_Card]):

    _cards: list[T_Card] = []

    def __init__(self, card_class: type[T_Card], shuffle_deck: bool, **data) -> None:
        super().__init__(**data)
        for (
            subclass
        ) in card_class.__subclasses__():  # pyright: ignore[reportAttributeAccessIssue]
            repetitions: int = subclass.model_fields["repetitions"].default
            for i in range(repetitions):
                card = subclass()  # pyright: ignore[reportCallIssue]
                self.add_repetition_to_card_name(card, i)
                self._cards.append(card)
        if shuffle_deck:
            shuffle(self._cards)

    @property
    def cards(self) -> list[T_Card]:
        return self._cards

    @staticmethod
    def add_repetition_to_card_name(card: BaseCard, repetition: int):
        card.name += f"__{repetition}"
