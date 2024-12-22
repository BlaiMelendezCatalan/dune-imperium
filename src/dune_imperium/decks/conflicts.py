from enum import Enum


class ConflictNumber(Enum):

    ONE = "I"
    TWO = "II"
    THREE = "III"


class ConflictCard:

    conflict_number: ConflictNumber

    def first_prize(self, player_id: int) -> None:
        pass

    def second_prize(self, player_id: int) -> None:
        pass

    def third_prize(self, player_id: int) -> None:
        pass


class BattleForArrakeen(ConflictCard):

    name = "battle_for_arrakeen"
    conflict_number = ConflictNumber.THREE


class BattleForCarthag(ConflictCard):

    name = "battle_for_carthag"
    conflict_number = ConflictNumber.THREE


class BattleForImperialBasin(ConflictCard):

    name = "battle_for_imperial_basin"
    conflict_number = ConflictNumber.THREE


class CloakAndDagger(ConflictCard):

    name = "cloak_and_dagger"
    conflict_number = ConflictNumber.TWO


class DesertPower(ConflictCard):

    name = "desert_power"
    conflict_number = ConflictNumber.TWO


class GrandVision(ConflictCard):

    name = "grand_vision"
    conflict_number = ConflictNumber.THREE


class GuildBankRaid(ConflictCard):

    name = "guild_bank_raid"
    conflict_number = ConflictNumber.TWO


class Machinations(ConflictCard):

    name = "machinations"
    conflict_number = ConflictNumber.TWO


class RaidStockpiles(ConflictCard):

    name = "raid_stockpiles"
    conflict_number = ConflictNumber.TWO


class SecureImperialBasin(ConflictCard):

    name = "secure_imperial_basin"
    conflict_number = ConflictNumber.TWO


class SiegeOfArrakeen(ConflictCard):

    name = "siege_of_carthag"
    conflict_number = ConflictNumber.TWO


class SiegeOfCarthag(ConflictCard):

    name = "siege_of_carthag"
    conflict_number = ConflictNumber.TWO


class SkirmishA(ConflictCard):

    name = "skirmish_a"
    conflict_number = ConflictNumber.ONE


class SkirmishB(ConflictCard):

    name = "skirmish_b"
    conflict_number = ConflictNumber.ONE


class SkirmishC(ConflictCard):

    name = "skirmish_c"
    conflict_number = ConflictNumber.ONE


class SkirmishD(ConflictCard):

    name = "skirmish_d"
    conflict_number = ConflictNumber.ONE


class SortThroughTheChaos(ConflictCard):

    name = "sort_through_the_chaos"
    conflict_number = ConflictNumber.TWO


class TerriblePurpose(ConflictCard):

    name = "terrible_purpose"
    conflict_number = ConflictNumber.TWO
