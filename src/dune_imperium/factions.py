from enum import Enum


class Faction(Enum):

    FREMEN = "fremen"
    BENE_GESSERIT = "bene_gesserit"
    SPACING_GUILD = "spacing_guild"
    EMPEROR = "emperor"


class Factions:

    def __init__(self, *factions: Faction):
        self._factions = list(factions)

    @property
    def factions(self) -> list[Faction]:
        return self._factions
