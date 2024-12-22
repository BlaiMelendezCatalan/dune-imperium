from enum import Enum


class IntrigueType(Enum):

    PLOT = "plot"
    COMBAT = "combat"
    ENDGAME = "endgame"


class IntrigueTypes:

    intrigue_types: list[IntrigueType]

    def __init__(self, *intrigue_types: IntrigueType):
        self.intrigue_types = list(intrigue_types)


class IntrigueCard:

    name: str
    repetitions: int = 1
    intrigue_types: IntrigueTypes

    def effect(self) -> None:
        # TODO trigger the effect of the intrigue card
        pass


class AlliedArmada(IntrigueCard):

    name = "allied_armada"
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class Ambush(IntrigueCard):

    name = "ambush"
    repetitions = 2
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class BinduSuspension(IntrigueCard):

    name = "bindu_suspension"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Bribery(IntrigueCard):

    name = "bribery"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class BypassProtocol(IntrigueCard):

    name = "bypass_protocol"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class CalculatedHire(IntrigueCard):

    name = "calculated_hire"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Charisma(IntrigueCard):

    name = "charisma"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class ChoamShares(IntrigueCard):

    name = "choam_shares"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class CouncilorsDispensation(IntrigueCard):

    name = "councilors_dispensation"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class CornerTheMarket(IntrigueCard):

    name = "corner_the_market"
    intrigue_types = IntrigueTypes(IntrigueType.ENDGAME)


class DemandRespect(IntrigueCard):

    name = "demand_respect"
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class DispatchAnEnvoy(IntrigueCard):

    name = "dispatch_an_envoy"
    repetitions = 2
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class DoubleCross(IntrigueCard):

    name = "double_cross"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class FavoredSubject(IntrigueCard):

    name = "favored_subject"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class GuildAuthorization(IntrigueCard):

    name = "guild_authorization"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Infiltrate(IntrigueCard):

    name = "infiltrate"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class KnowTheirWays(IntrigueCard):

    name = "know_their_ways"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class MasterTactician(IntrigueCard):

    name = "master_tactician"
    repetitions = 3
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class PlansWithinPlans(IntrigueCard):

    name = "plans_within_plans"
    intrigue_types = IntrigueTypes(IntrigueType.ENDGAME)


class PoisonDetector(IntrigueCard):

    name = "poison_detector"
    repetitions = 2
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class PrivateArmy(IntrigueCard):

    name = "private_army"
    repetitions = 2
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class RapidMovilization(IntrigueCard):

    name = "rapid_movilization"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class RecruitmentMission(IntrigueCard):

    name = "recruitment_mission"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Reinforcements(IntrigueCard):

    name = "reinforcements"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Refocus(IntrigueCard):

    name = "refocus"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class SecretsOfTheSisterhood(IntrigueCard):

    name = "secrets_of_the_sisterhood"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class StagedIncident(IntrigueCard):

    name = "staged_incident"
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class TheSleeperMustAwaken(IntrigueCard):

    name = "the_sleeper_must_awaken"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Tiebreaker(IntrigueCard):

    name = "tiebreaker"
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT, IntrigueType.ENDGAME)


class ToTheVictor(IntrigueCard):

    name = "to_the_victor"
    intrigue_types = IntrigueTypes(IntrigueType.COMBAT)


class UrgentMission(IntrigueCard):

    name = "urgent_mission"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class WaterOfLife(IntrigueCard):

    name = "water_of_life"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class WaterPeddlersUnion(IntrigueCard):

    name = "water_peddlers_union"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class Windfall(IntrigueCard):

    name = "windfall"
    intrigue_types = IntrigueTypes(IntrigueType.PLOT)


class IntrigueDeck:

    cards: list[IntrigueCard]

    def initialize(self):
        self.cards = [
            subclass()
            for subclass in IntrigueCard.__subclasses__()
            for _ in range(subclass.repetitions)
        ]
