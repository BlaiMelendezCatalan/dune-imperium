import random
from pydantic import BaseModel

from dune_imperium.decks.conflicts import ConflictDeck
from dune_imperium.decks.imperium import ImperiumDeck
from dune_imperium.decks.intrigue import IntrigueDeck
from dune_imperium.decks.reserve import (
    ArrakisLiaisonDeck,
    FoldSpaceDeck,
    TheSpiceMustFlowDeck,
)
from dune_imperium.map.locations import Locations
from dune_imperium.player import Player
from dune_imperium.decks.leaders import (
    PaulAtreides,
    GlossuRabban,
    CountessArianaThorvald,
)


class Game(BaseModel):

    name: str

    players: dict[int, Player] = {  # TODO these are hardcoded values to make it work
        0: Player(id=0, leader=PaulAtreides(), victory_points=0),
        1: Player(id=1, leader=GlossuRabban(), victory_points=0),
        2: Player(id=2, leader=CountessArianaThorvald(), victory_points=0),
    }

    first_player: int = random.randint(0, len(players) - 1)

    round: int = 1

    map: Locations = Locations()

    imperium_deck: ImperiumDeck = ImperiumDeck()
    intrigue_deck: IntrigueDeck = IntrigueDeck()
    conflict_deck: ConflictDeck = ConflictDeck()
    arrakis_liaison_deck: ArrakisLiaisonDeck = ArrakisLiaisonDeck()
    fold_space_deck: FoldSpaceDeck = FoldSpaceDeck()
    the_spice_must_flow_deck: TheSpiceMustFlowDeck = TheSpiceMustFlowDeck()

    def round_start(self) -> None:
        # A new conflict card is exposed
        self.conflict_deck.trash_exposed()
        self.conflict_deck.cards[self.round - 1].expose()

        # Players draw 5 cards
        [player.hand.draw() for player in list(self.players.values())]

    def player_turns(self) -> None: ...

    def combat(self) -> None: ...

    def makers(self) -> None:
        [spice_location.produce_spice() for spice_location in self.map.spice_locations]

    def recall(self) -> None:
        if self.round == 10 or any(
            [player.victory_points >= 10 for player in list(self.players.values())]
        ):
            # Play endgame intrigue cards
            # Get players victory points
            # If draw check other conditions
            # Declare winner
            return

        # Return mentat
        # Return agents
        # Change first player

        self.first_player = (self.first_player + 1) % 3
        self.round += 1
