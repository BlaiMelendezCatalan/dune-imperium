from pydantic import BaseModel

from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.factions import Faction
from dune_imperium.agent_icons.icons import AgentIcon


class ImperiumCard(BaseBigCard):

    factions: list[Faction] = []
    persuasion_cost: int


class ArrakisRecruiter(ImperiumCard):

    name: str = "arrakis_recruiter"
    repetitions: int = 2
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class AssassinationMission(ImperiumCard):

    name: str = "assassination_mission"
    repetitions: int = 2
    persuasion_cost: int = 1


class BeneGesseritInitiate(ImperiumCard):

    name: str = "bene_gesserit_initiate"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]


class BeneGesseritSister(ImperiumCard):

    name: str = "bene_gesserit_sister"
    repetitions: int = 3
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.LANDSRAAT]


class Carryall(ImperiumCard):

    name: str = "carryall"
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]


class Chani(ImperiumCard):

    name: str = "chani"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic


class ChoamDirectorship(ImperiumCard):

    name: str = "choam_directorship"
    persuasion_cost: int = 8

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic


class Crysknife(ImperiumCard):

    name: str = "crysknife"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]


class DoctorYueh(ImperiumCard):

    name: str = "doctor_yueh"
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class DuncanIdaho(ImperiumCard):

    name: str = "duncan_idaho"
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class FedaykinDeathCommando(ImperiumCard):

    name: str = "fedaykin_death_commando"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]


class FirmGrip(ImperiumCard):

    name: str = "firm_grip"
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]


class FremenCamp(ImperiumCard):

    name: str = "fremen_camp"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]


class GeneManipulation(ImperiumCard):

    name: str = "gene_manipulation"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]


class GuildAdministrator(ImperiumCard):

    name: str = "guild_administrator"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD, AgentIcon.SPICE_TRADE]


class GuildAmbassador(ImperiumCard):

    name: str = "guild_ambassador"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]


class GuildBankers(ImperiumCard):

    name: str = "guild_bankers"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.LANDSRAAT,
    ]


class GunThopter(ImperiumCard):

    name: str = "gun_thopter"
    repetitions: int = 2
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]


class GurneyHalleck(ImperiumCard):

    name: str = "gurney_halleck"
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]


class ImperialSpy(ImperiumCard):

    name: str = "imperial_spy"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]


class KwisatzHaderach(ImperiumCard):

    name: str = "kwisatz_haderach"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 8
    agent_icons: list[AgentIcon] = []

    def revelation_reward(self, player_id: int) -> None:
        pass


class LadyJessica(ImperiumCard):

    name: str = "lady_jessica"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 7
    agent_icons: list[AgentIcon] = [
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def agent_reward(self, player_id: int): ...


class LietKynes(ImperiumCard):

    name: str = "liet_kynes"
    factions: list[Faction] = [Faction.EMPEROR, Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.CITY]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def agent_reward(self, player_id: int): ...


class MissionariaProtectiva(ImperiumCard):

    name: str = "missionaria_protectiva"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def agent_reward(self, player_id: int): ...


class Opulence(ImperiumCard):

    name: str = "opulence"
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]

    def agent_reward(self, player_id: int): ...


class OtherMemory(ImperiumCard):

    name: str = "other_memory"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def agent_reward(self, player_id: int): ...


class PiterDeVries(ImperiumCard):

    name: str = "piter_de_vries"
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def agent_reward(self, player_id: int): ...


class PowerPlay(ImperiumCard):

    name: str = "power_play"
    repetitions: int = 3
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def agent_reward(self, player_id: int): ...

    def revelation_reward(self, player_id: int) -> None:
        pass


class ReverendMotherMohiam(ImperiumCard):

    name: str = "reverend_mother_mohiam"
    factions: list[Faction] = [Faction.EMPEROR, Faction.BENE_GESSERIT]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.BENE_GESSERIT]

    def agent_reward(self, player_id: int): ...


class SardaukarInfantry(ImperiumCard):

    name: str = "sardaukar_infantry"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = []

    def agent_reward(self, player_id: int): ...


class SardaukarLegion(ImperiumCard):

    name: str = "sardaukar_legion"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]

    def agent_reward(self, player_id: int): ...


class Scout(ImperiumCard):

    name: str = "scout"
    repetitions: int = 2
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def agent_reward(self, player_id: int): ...


class ShiftingAllegiances(ImperiumCard):

    name: str = "shifting_allegiances"
    repetitions: int = 2
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.SPICE_TRADE]

    def agent_reward(self, player_id: int): ...


class SietchReverendMother(ImperiumCard):

    name: str = "sietch_reverend_mother"
    factions: list[Faction] = [Faction.BENE_GESSERIT, Faction.FREMEN]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.FREMEN]

    def agent_reward(self, player_id: int): ...


class SmugglersThopter(ImperiumCard):

    name: str = "smugglers_thopter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def agent_reward(self, player_id: int): ...


class SpaceTravel(ImperiumCard):

    name: str = "space_travel"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD]

    def agent_reward(self, player_id: int): ...


class SpiceHunter(ImperiumCard):

    name: str = "spice_hunter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]

    def agent_reward(self, player_id: int): ...


class SpiceSmugglers(ImperiumCard):

    name: str = "spice_smugglers"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def agent_reward(self, player_id: int): ...


class Stilgar(ImperiumCard):

    name: str = "stilgar"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def agent_reward(self, player_id: int): ...


class TesteOfHumanity(ImperiumCard):

    name: str = "test_of_humanity"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
    ]


class TheVoice(ImperiumCard):

    name: str = "the_voice"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]


class ThufirHawat(ImperiumCard):

    name: str = "thufir_hawat"
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]


class WormRiders(ImperiumCard):

    name: str = "worm_riders"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]


class ImperiumDeck(BaseDeck[ImperiumCard]):

    def __init__(self, **data) -> None:
        super().__init__(ImperiumCard, shuffle_deck=True, **data)


class ImperiumExposedDeck(BaseModel):

    cards: dict[str, ImperiumCard] = {}

    def add(self, cards: list[ImperiumCard]):
        self.cards.update({card.name: card for card in cards})

    def pop(self, card_name: str) -> ImperiumCard:
        return self.cards[card_name]
