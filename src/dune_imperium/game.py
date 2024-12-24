from pydantic import BaseModel

from dune_imperium.decks.conflicts import ConflictDeck
from dune_imperium.decks.imperium import ImperiumDeck
from dune_imperium.decks.intrigue import IntrigueDeck
from dune_imperium.decks.reserve import (
    ArrakisLiaisonDeck,
    FoldSpaceDeck,
    TheSpiceMustFlowDeck,
)
from dune_imperium.player import Player
from dune_imperium.decks.leaders import (
    PaulAtreides,
    GlossuRabban,
    CountessArianaThorvald,
)
from dune_imperium.map.dune_map import DuneMap


class Game(BaseModel):

    name: str

    players: dict[str, Player] = {  # TODO these are hardcoded values to make it work
        "player_1": Player(
            id=1, leader=PaulAtreides(), victory_points=0, first_player=True
        ),
        "player_2": Player(
            id=2, leader=GlossuRabban(), victory_points=0, first_player=False
        ),
        "player_3": Player(
            id=3, leader=CountessArianaThorvald(), victory_points=0, first_player=False
        ),
    }

    dune_map: DuneMap = DuneMap()

    imperium_deck = ImperiumDeck()
    intrigue_deck = IntrigueDeck()
    conflict_deck = ConflictDeck()
    arrakis_liaison_deck = ArrakisLiaisonDeck()
    fold_space_deck = FoldSpaceDeck()
    the_spice_must_flow_deck = TheSpiceMustFlowDeck()
