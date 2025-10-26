from typing import TYPE_CHECKING

from pydantic import BaseModel

if TYPE_CHECKING:
    from dune_imperium.player import Player


MAX_INFLUENCE = 6


class InfluenceTracker(BaseModel):

    influence: int = 0

    def increase_influence(self, player: "Player") -> None:
        # TODO
        pass

    def decrease_influence(self, player: "Player") -> None:
        # TODO
        pass
