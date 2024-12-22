from dune_imperium.decks.imperium import ImperiumCard
from dune_imperium.decks.initial import InitialCard, InitialDeck


class PlayerDeck:

    cards: list[ImperiumCard | InitialCard]

    def initialize(self) -> None:
        initial_deck = InitialDeck()
        initial_deck.initialize()
        self.cards = list(initial_deck.cards)

    def rebuild(self, *cards: InitialCard | ImperiumCard) -> None:
        # TODO get all cards in discard pile and shuffle
        ...


class PlayerHand:

    cards: list[ImperiumCard | InitialCard]

    def draw(self, *cards: InitialCard | ImperiumCard) -> None:
        self.cards = list(cards)

    def play(self, card: InitialCard | ImperiumCard) -> None:
        # TODO
        ...

    def trash(self, card: InitialCard | ImperiumCard) -> None:
        # TODO
        ...


class InPlay:

    cards: list[ImperiumCard | InitialCard]

    def add(self, card: InitialCard | ImperiumCard):
        # TODO
        ...

    def discard(self) -> None:
        # TODO
        ...


class DiscardPile:

    cards: list[ImperiumCard | InitialCard] = []

    def add(self, card: InitialCard | ImperiumCard):
        # TODO
        ...

    def trash(self, card: InitialCard | ImperiumCard) -> None:
        # TODO
        ...
