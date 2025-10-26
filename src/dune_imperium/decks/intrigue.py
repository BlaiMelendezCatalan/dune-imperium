from enum import Enum
from typing import Self

from dune_imperium.decks.base import BaseCard, BaseSourceDeck


class IntrigueType(str, Enum):

    PLOT = "plot"
    COMBAT = "combat"
    ENDGAME = "endgame"


class IntrigueCard(BaseCard):

    intrigue_types: list[IntrigueType]

    def play(self) -> None:
        # TODO trigger the effect of the intrigue card through the API and remove it from player Intrigues deck
        pass


class AlliedArmada(IntrigueCard):

    name: str = "allied_armada"
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class Ambush(IntrigueCard):

    name: str = "ambush"
    repetitions: int = 2
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class BinduSuspension(IntrigueCard):

    name: str = "bindu_suspension"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Bribery(IntrigueCard):

    name: str = "bribery"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class BypassProtocol(IntrigueCard):

    name: str = "bypass_protocol"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class CalculatedHire(IntrigueCard):

    name: str = "calculated_hire"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Charisma(IntrigueCard):

    name: str = "charisma"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class ChoamShares(IntrigueCard):

    name: str = "choam_shares"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class CouncilorsDispensation(IntrigueCard):

    name: str = "councilors_dispensation"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class CornerTheMarket(IntrigueCard):

    name: str = "corner_the_market"
    intrigue_types: list[IntrigueType] = [IntrigueType.ENDGAME]


class DemandRespect(IntrigueCard):

    name: str = "demand_respect"
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class DispatchAnEnvoy(IntrigueCard):

    name: str = "dispatch_an_envoy"
    repetitions: int = 2
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class DoubleCross(IntrigueCard):

    name: str = "double_cross"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class FavoredSubject(IntrigueCard):

    name: str = "favored_subject"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class GuildAuthorization(IntrigueCard):

    name: str = "guild_authorization"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Infiltrate(IntrigueCard):

    name: str = "infiltrate"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class KnowTheirWays(IntrigueCard):

    name: str = "know_their_ways"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class MasterTactician(IntrigueCard):

    name: str = "master_tactician"
    repetitions: int = 3
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class PlansWithinPlans(IntrigueCard):

    name: str = "plans_within_plans"
    intrigue_types: list[IntrigueType] = [IntrigueType.ENDGAME]


class PoisonDetector(IntrigueCard):

    name: str = "poison_detector"
    repetitions: int = 2
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class PrivateArmy(IntrigueCard):

    name: str = "private_army"
    repetitions: int = 2
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class RapidMovilization(IntrigueCard):

    name: str = "rapid_movilization"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class RecruitmentMission(IntrigueCard):

    name: str = "recruitment_mission"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Reinforcements(IntrigueCard):

    name: str = "reinforcements"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Refocus(IntrigueCard):

    name: str = "refocus"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class SecretsOfTheSisterhood(IntrigueCard):

    name: str = "secrets_of_the_sisterhood"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class StagedIncident(IntrigueCard):

    name: str = "staged_incident"
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class TheSleeperMustAwaken(IntrigueCard):

    name: str = "the_sleeper_must_awaken"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Tiebreaker(IntrigueCard):

    name: str = "tiebreaker"
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT, IntrigueType.ENDGAME]


class ToTheVictor(IntrigueCard):

    name: str = "to_the_victor"
    intrigue_types: list[IntrigueType] = [IntrigueType.COMBAT]


class UrgentMission(IntrigueCard):

    name: str = "urgent_mission"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class WaterOfLife(IntrigueCard):

    name: str = "water_of_life"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class WaterPeddlersUnion(IntrigueCard):

    name: str = "water_peddlers_union"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class Windfall(IntrigueCard):

    name: str = "windfall"
    intrigue_types: list[IntrigueType] = [IntrigueType.PLOT]


class IntrigueDeck(BaseSourceDeck[IntrigueCard]):

    def initialize(self) -> Self:
        super()._initialize(IntrigueCard)
        return self
