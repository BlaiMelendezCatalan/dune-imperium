from enum import Enum


class CardState(Enum):

    IN_DECK = "in_deck"
    EXPOSED = "exposed"
    ACQUIRED = "acquired"
    TRASHED = "trashed"
