import random
from pydantic import BaseModel

from dune_imperium.decks.conflicts import ConflictCard, ConflictDeck
from dune_imperium.decks.imperium import ImperiumDeck, ImperiumExposedDeck
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
    imperium_exposed_deck: ImperiumExposedDeck = ImperiumExposedDeck()
    intrigue_deck: IntrigueDeck = IntrigueDeck()
    conflict_deck: ConflictDeck = ConflictDeck()
    conflict_in_play: ConflictCard | None = None
    arrakis_liaison_deck: ArrakisLiaisonDeck = ArrakisLiaisonDeck()
    fold_space_deck: FoldSpaceDeck = FoldSpaceDeck()
    the_spice_must_flow_deck: TheSpiceMustFlowDeck = TheSpiceMustFlowDeck()

    def setup(self) -> None:
        # Expose first 5 imperium cards
        self.imperium_exposed_deck.initialize(self.imperium_deck.cards)

        # TODO think what to do with the reserve

    def round_start(self) -> None:
        # A new conflict card is exposed
        conflict_card = self.conflict_deck.cards.pop(0)
        self.conflict_in_play = conflict_card
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

    def move_exposed_imperium_card_to_player_discard_pile(
        self, player_id: int, card_name: str
    ) -> None:
        imperium_card = self.imperium_exposed_deck.cards[card_name]
        self.players[player_id].discard_pile.add(imperium_card)

    def expose_next_imperium_card(self) -> None:
        imperium_card = self.imperium_deck.cards.pop(0)
        self.imperium_exposed_deck.add(imperium_card)
