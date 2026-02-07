from typing import TYPE_CHECKING

from pydantic import BaseModel

from dune_imperium.map.locations import Location

if TYPE_CHECKING:
    from dune_imperium.game import Game
    from dune_imperium.player import Player


class Agent(BaseModel):

    deployed: bool = False
    location: Location | None = None

    def deploy(self, location: Location, player: "Player", game: "Game") -> None:
        self.deployed = True
        self.location = location
        self.location.pay(player, game)
        # TODO run location methods passing player_id as a parameter
        # - run location.pay or tell user it is not possible
        # - run location.reward
        # - run location.control.add_resource

    def recall(self) -> None:
        self.deployed = False
        self.location = None
