from enum import Enum
from pydantic import BaseModel
from random import shuffle

from dune_imperium.decks.card_states import CardState


class ConflictNumber(Enum):

    ONE = "I"
    TWO = "II"
    THREE = "III"


class ConflictCard(BaseModel):

    name: str
    conflict_number: ConflictNumber
    state: CardState = CardState.IN_DECK

    def expose(self) -> None:
        if self.state == CardState.IN_DECK:
            self.state = CardState.EXPOSED
        else:
            raise RuntimeError("Only in-deck card can be exposed.")

    def trash(self) -> None:
        if self.state == CardState.EXPOSED:
            self.state = CardState.TRASHED
        else:
            raise RuntimeError("Only exposed card can be trashed.")

    def first_prize(self, player_id: int) -> None:
        pass

    def second_prize(self, player_id: int) -> None:
        pass

    def third_prize(self, player_id: int) -> None:
        pass


class BattleForArrakeen(ConflictCard):

    name: str = "battle_for_arrakeen"
    conflict_number: ConflictNumber = ConflictNumber.THREE


class BattleForCarthag(ConflictCard):

    name: str = "battle_for_carthag"
    conflict_number: ConflictNumber = ConflictNumber.THREE


class BattleForImperialBasin(ConflictCard):

    name: str = "battle_for_imperial_basin"
    conflict_number: ConflictNumber = ConflictNumber.THREE


class CloakAndDagger(ConflictCard):

    name: str = "cloak_and_dagger"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class DesertPower(ConflictCard):

    name: str = "desert_power"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class GrandVision(ConflictCard):

    name: str = "grand_vision"
    conflict_number: ConflictNumber = ConflictNumber.THREE


class GuildBankRaid(ConflictCard):

    name: str = "guild_bank_raid"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class Machinations(ConflictCard):

    name: str = "machinations"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class RaidStockpiles(ConflictCard):

    name: str = "raid_stockpiles"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class SecureImperialBasin(ConflictCard):

    name: str = "secure_imperial_basin"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class SiegeOfArrakeen(ConflictCard):

    name: str = "siege_of_carthag"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class SiegeOfCarthag(ConflictCard):

    name: str = "siege_of_carthag"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class SkirmishA(ConflictCard):

    name: str = "skirmish_a"
    conflict_number: ConflictNumber = ConflictNumber.ONE


class SkirmishB(ConflictCard):

    name: str = "skirmish_b"
    conflict_number: ConflictNumber = ConflictNumber.ONE


class SkirmishC(ConflictCard):

    name: str = "skirmish_c"
    conflict_number: ConflictNumber = ConflictNumber.ONE


class SkirmishD(ConflictCard):

    name: str = "skirmish_d"
    conflict_number: ConflictNumber = ConflictNumber.ONE


class SortThroughTheChaos(ConflictCard):

    name: str = "sort_through_the_chaos"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class TerriblePurpose(ConflictCard):

    name: str = "terrible_purpose"
    conflict_number: ConflictNumber = ConflictNumber.TWO


class ConflictDeck(BaseModel):

    cards: list[ConflictCard] = []

    def __init__(self, **data) -> None:
        super().__init__(**data)
        cards_dict: dict[ConflictNumber, list[ConflictCard]] = {
            ConflictNumber.ONE: [],
            ConflictNumber.TWO: [],
            ConflictNumber.THREE: [],
        }
        for subclass in ConflictCard.__subclasses__():
            cards_dict[subclass.model_fields["conflict_number"].default].append(
                subclass()  # pyright: ignore[reportCallIssue]
            )

        shuffle(cards_dict[ConflictNumber.ONE])
        shuffle(cards_dict[ConflictNumber.TWO])
        shuffle(cards_dict[ConflictNumber.THREE])

        self.cards = [card for card in cards_dict[ConflictNumber.ONE][:1]]
        self.cards += [card for card in cards_dict[ConflictNumber.TWO][:5]]
        self.cards += [card for card in cards_dict[ConflictNumber.THREE]]

    def trash_exposed(self) -> None:
        [card.trash() for card in self.cards if card.state == CardState.EXPOSED]
