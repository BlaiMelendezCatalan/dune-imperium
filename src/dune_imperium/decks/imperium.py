import httpx

from dune_imperium.decks.base import BaseBigCard, BaseDeck
from dune_imperium.decks.card_states import CardState
from dune_imperium.decks.factions import Faction
from dune_imperium.agent_icons.icons import AgentIcon


class ImperiumCard(BaseBigCard):

    factions: list[Faction] = []
    cost: int
    state: CardState = CardState.IN_DECK

    def acquire(self, player_id: int) -> None:
        # TODO check exposed. Remove from imperium deck and place in player's discard deck. Apply any necessary logic
        ...

    def expose(self):
        self.state = CardState.EXPOSED

    def play_as_agent(self, player_id: int) -> None:
        httpx.post("http://127.0.0.1:5432/")  # TODO fix

    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass

    def trash(self):
        # TODO
        pass


class ArrakisRecruiter(ImperiumCard):

    name: str = "arrakis_recruiter"
    repetitions: int = 2
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class AssassinationMission(ImperiumCard):

    name: str = "assassination_mission"
    repetitions: int = 2
    cost: int = 1

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class BeneGesseritInitiate(ImperiumCard):

    name: str = "bene_gesserit_initiate"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class BeneGesseritSister(ImperiumCard):

    name: str = "bene_gesserit_sister"
    repetitions: int = 3
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Carryall(ImperiumCard):

    name: str = "carryall"
    cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Chani(ImperiumCard):

    name: str = "chani"
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ChoamDirectorship(ImperiumCard):

    name: str = "choam_directorship"
    cost: int = 8

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Crysknife(ImperiumCard):

    name: str = "crysknife"
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DoctorYueh(ImperiumCard):

    name: str = "doctor_yueh"
    cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DuncanIdaho(ImperiumCard):

    name: str = "duncan_idaho"
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FedaykinDeathCommando(ImperiumCard):

    name: str = "fedaykin_death_commando"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FirmGrip(ImperiumCard):

    name: str = "firm_grip"
    factions: list[Faction] = [Faction.EMPEROR]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FremenCamp(ImperiumCard):

    name: str = "fremen_camp"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GeneManipulation(ImperiumCard):

    name: str = "gene_manipulation"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildAdministrator(ImperiumCard):

    name: str = "guild_administrator"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildAmbassador(ImperiumCard):

    name: str = "guild_ambassador"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildBankers(ImperiumCard):

    name: str = "guild_bankers"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.LANDSRAAT,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GunThopter(ImperiumCard):

    name: str = "gun_thopter"
    repetitions: int = 2
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GurneyHalleck(ImperiumCard):

    name: str = "gurney_halleck"
    cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ImperialSpy(ImperiumCard):

    name: str = "imperial_spy"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class KwisatzHaderach(ImperiumCard):

    name: str = "kwisatz_haderach"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 8
    agent_icons: list[AgentIcon] = []

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None:
        pass


class LadyJessica(ImperiumCard):

    name: str = "lady_jessica"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 7
    agent_icons: list[AgentIcon] = [
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class LietKynes(ImperiumCard):

    name: str = "liet_kynes"
    factions: list[Faction] = [Faction.EMPEROR, Faction.FREMEN]
    cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.CITY]

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class MissionariaProtectiva(ImperiumCard):

    name: str = "missionaria_protectiva"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Opulence(ImperiumCard):

    name: str = "opulence"
    factions: list[Faction] = [Faction.EMPEROR]
    cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class OtherMemory(ImperiumCard):

    name: str = "other_memory"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class PiterDeVries(ImperiumCard):

    name: str = "piter_de_vries"
    cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class PowerPlay(ImperiumCard):

    name: str = "power_play"
    repetitions: int = 3
    cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    ]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None:
        pass


class ReverendMotherMohiam(ImperiumCard):

    name: str = "reverend_mother_mohiam"
    factions: list[Faction] = [Faction.EMPEROR, Faction.BENE_GESSERIT]
    cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.BENE_GESSERIT]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SardaukarInfantry(ImperiumCard):

    name: str = "sardaukar_infantry"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    cost: int = 1
    agent_icons: list[AgentIcon] = []

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SardaukarLegion(ImperiumCard):

    name: str = "sardaukar_legion"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Scout(ImperiumCard):

    name: str = "scout"
    repetitions: int = 2
    cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ShiftingAllegiances(ImperiumCard):

    name: str = "shifting_allegiances"
    repetitions: int = 2
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SietchReverendMother(ImperiumCard):

    name: str = "sietch_reverend_mother"
    factions: list[Faction] = [Faction.BENE_GESSERIT, Faction.FREMEN]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.FREMEN]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SmugglersThopter(ImperiumCard):

    name: str = "smugglers_thopter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpaceTravel(ImperiumCard):

    name: str = "space_travel"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpiceHunter(ImperiumCard):

    name: str = "spice_hunter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpiceSmugglers(ImperiumCard):

    name: str = "spice_smugglers"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Stilgar(ImperiumCard):

    name: str = "stilgar"
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TesteOfHumanity(ImperiumCard):

    name: str = "test_of_humanity"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TheVoice(ImperiumCard):

    name: str = "the_voice"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ThufirHawat(ImperiumCard):

    name: str = "thufir_hawat"
    cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class WormRiders(ImperiumCard):

    name: str = "worm_riders"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ImperiumDeck(BaseDeck[ImperiumCard]):

    def __init__(self, **data) -> None:
        super().__init__(ImperiumCard, shuffle_deck=True, **data)
