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

    round: int = 1

    first_player: int = random.randint(0, len(players) - 1)

    current_player: int | None = None

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
        self.expose_n_imperium_cards(n=5)
        # Set first player as current player
        self.current_player = self.first_player

    def round_start(self) -> None:
        # A new conflict card is exposed
        self.conflict_in_play = self.conflict_deck.cards.pop(0)
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
        self.current_player = self.first_player
        self.round += 1

    def acquire_exposed_card(self, player_id: int, card_name: str) -> None:
        if "arrakis_liaison" in card_name:
            arrakis_liaison_card = self.arrakis_liaison_deck.cards.pop(0)
            self.players[player_id].discard_pile.add(arrakis_liaison_card)
        elif "fold_space" in card_name:
            fold_space_card = self.arrakis_liaison_deck.cards.pop(0)
            self.players[player_id].discard_pile.add(fold_space_card)
        elif "the_spice_must_flow" in card_name:
            the_spice_must_flow_card = self.arrakis_liaison_deck.cards.pop(0)
            self.players[player_id].discard_pile.add(the_spice_must_flow_card)
        elif imperium_card := self.imperium_exposed_deck.cards.get(card_name):
            self.players[player_id].discard_pile.add(imperium_card)
        else:
            raise ValueError(f"No exposed card with name: {card_name}.")

    def expose_n_imperium_cards(self, n: int) -> None:
        imperium_cards = [self.imperium_deck.cards.pop(0) for _ in range(n)]
        self.imperium_exposed_deck.add(imperium_cards)
