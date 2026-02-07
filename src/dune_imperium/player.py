from pydantic import BaseModel, model_validator

from dune_imperium.decks.leaders import Leader
from dune_imperium.decks.player import (
    PlayerDecks,
)
from dune_imperium.elements.tokens.agents import Agent
from dune_imperium.elements.tokens.resources import Resources
from dune_imperium.elements.tokens.troops import TroopPool
from dune_imperium.utils.utils import all_subclasses, item_name_to_item_class_name


class Player(BaseModel):

    id: int

    leader: Leader

    resources: Resources = Resources()

    persuasion: int = 0
    swords: int = 0

    agents: list[Agent] = [Agent() for _ in range(2)]

    troops: TroopPool = TroopPool()

    decks: PlayerDecks = PlayerDecks()

    @model_validator(mode="before")
    def resolve_leader_class(cls, values):
        leader = values.get("leader", {})
        if issubclass(type(leader), Leader):
            return values
        leader_name = item_name_to_item_class_name(leader["name"])
        for subclass in all_subclasses(Leader):
            if subclass.__name__ == leader_name:
                leader = subclass(**leader)
                values.update({"leader": leader})
                break
        else:
            raise ValueError(f"Leader class not found for leader: {leader_name}")

        return values
