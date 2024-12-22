from abc import ABC, abstractmethod
from random import shuffle

from dune_imperium.factions import Faction, Factions
from dune_imperium.icons import AgentIcon, AgentIcons


class ImperiumCard(ABC):

    name: str
    repetitions: int = 1
    exposed: bool = False
    factions: Factions = Factions()
    cost: int
    agent_icons: AgentIcons = AgentIcons()

    def acquire(self, player_id: int) -> None:
        # TODO check exposed. Remove from imperium deck and place in player's discard deck. Apply any necessary logic
        ...

    def expose(self):
        self.exposed = True

    def trash(self):
        # TODO
        ...

    @abstractmethod
    def play_as_agent(self, player_id: int) -> None:
        # TODO apply logic and let the user decide the location of the agent.
        pass

    @abstractmethod
    def play_as_revelation(self, player_id: int) -> None:
        # TODO apply logic
        pass


class ArrakisRecruiter(ImperiumCard):

    name = "arrakis_recruiter"
    repetitions = 2
    cost = 2
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class AssassinationMission(ImperiumCard):

    name = "assassination_mission"
    repetitions = 2
    cost = 1

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class BeneGesseritInitiate(ImperiumCard):

    name = "bene_gesserit_initiate"
    repetitions = 2
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class BeneGesseritSister(ImperiumCard):

    name = "bene_gesserit_sister"
    repetitions = 3
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.BENE_GESSERIT, AgentIcon.LANDSRAAT)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Carryall(ImperiumCard):

    name = "carryall"
    cost = 5
    agent_icons = AgentIcons(AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Chani(ImperiumCard):

    name = "chani"
    factions = Factions(Faction.FREMEN)
    cost = 5
    agent_icons = AgentIcons(AgentIcon.FREMEN, AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ChoamDirectorship(ImperiumCard):

    name = "choam_directorship"
    cost = 8

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Crysknife(ImperiumCard):

    name = "crysknife"
    factions = Factions(Faction.FREMEN)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.FREMEN, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DoctorYueh(ImperiumCard):

    name = "doctor_yueh"
    cost = 1
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class DuncanIdaho(ImperiumCard):

    name = "duncan_idaho"
    cost = 4
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FedaykinDeathCommando(ImperiumCard):

    name = "fedaykin_death_commando"
    repetitions = 2
    factions = Factions(Faction.FREMEN)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FirmGrip(ImperiumCard):

    name = "firm_grip"
    factions = Factions(Faction.EMPEROR)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.EMPEROR, AgentIcon.LANDSRAAT)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class FremenCamp(ImperiumCard):

    name = "fremen_camp"
    repetitions = 2
    factions = Factions(Faction.FREMEN)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GeneManipulation(ImperiumCard):

    name = "gene_manipulation"
    repetitions = 2
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildAdministrator(ImperiumCard):

    name = "guild_administrator"
    repetitions = 2
    factions = Factions(Faction.SPACING_GUILD)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.SPACING_GUILD, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildAmbassador(ImperiumCard):

    name = "guild_ambassador"
    factions = Factions(Faction.SPACING_GUILD)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GuildBankers(ImperiumCard):

    name = "guild_bankers"
    factions = Factions(Faction.SPACING_GUILD)
    cost = 3
    agent_icons = AgentIcons(
        AgentIcon.EMPEROR, AgentIcon.SPACING_GUILD, AgentIcon.LANDSRAAT
    )

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GunThopter(ImperiumCard):

    name = "gun_thopter"
    repetitions = 2
    cost = 4
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class GurneyHalleck(ImperiumCard):

    name = "gurney_halleck"
    cost = 6
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ImperialSpy(ImperiumCard):

    name = "imperial_spy"
    repetitions = 2
    factions = Factions(Faction.EMPEROR)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.EMPEROR)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class KwisatzHaderach(ImperiumCard):

    name = "kwisatz_haderach"
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 8
    agent_icons = AgentIcons()

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None:
        pass


class LadyJessica(ImperiumCard):

    name = "lady_jessica"
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 7
    agent_icons = AgentIcons(
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    )

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class LietKynes(ImperiumCard):

    name = "liet_kynes"
    factions = Factions(Faction.EMPEROR, Faction.FREMEN)
    cost = 5
    agent_icons = AgentIcons(AgentIcon.FREMEN, AgentIcon.CITY)

    def acquire(self, player_id: int) -> None:
        super().acquire(player_id)
        # TODO Add extra logic

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class MissionariaProtectiva(ImperiumCard):

    name = "missionaria_protectiva"
    repetitions = 2
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 1
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Opulence(ImperiumCard):

    name = "opulence"
    factions = Factions(Faction.EMPEROR)
    cost = 6
    agent_icons = AgentIcons(AgentIcon.EMPEROR)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class OtherMemory(ImperiumCard):

    name = "other_memory"
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class PiterDeVries(ImperiumCard):

    name = "piter_de_vries"
    cost = 5
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.CITY)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class PowerPlay(ImperiumCard):

    name = "power_play"
    repetitions = 3
    cost = 5
    agent_icons = AgentIcons(
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
    )

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None:
        pass


class ReverendMotherMohiam(ImperiumCard):

    name = "reverend_mother_mohiam"
    factions = Factions(Faction.EMPEROR, Faction.BENE_GESSERIT)
    cost = 6
    agent_icons = AgentIcons(AgentIcon.EMPEROR, AgentIcon.BENE_GESSERIT)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SardaukarInfantry(ImperiumCard):

    name = "sardaukar_infantry"
    repetitions = 2
    factions = Factions(Faction.EMPEROR)
    cost = 1
    agent_icons = AgentIcons()

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SardaukarLegion(ImperiumCard):

    name = "sardaukar_legion"
    repetitions = 2
    factions = Factions(Faction.EMPEROR)
    cost = 5
    agent_icons = AgentIcons(AgentIcon.EMPEROR, AgentIcon.LANDSRAAT)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Scout(ImperiumCard):

    name = "scout"
    repetitions = 2
    cost = 1
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ShiftingAllegiances(ImperiumCard):

    name = "shifting_allegiances"
    repetitions = 2
    cost = 3
    agent_icons = AgentIcons(AgentIcon.LANDSRAAT, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SietchReverendMother(ImperiumCard):

    name = "sietch_reverend_mother"
    factions = Factions(Faction.BENE_GESSERIT, Faction.FREMEN)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.BENE_GESSERIT, AgentIcon.FREMEN)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SmugglersThopter(ImperiumCard):

    name = "smugglers_thopter"
    repetitions = 2
    factions = Factions(Faction.SPACING_GUILD)
    cost = 4
    agent_icons = AgentIcons(AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpaceTravel(ImperiumCard):

    name = "space_travel"
    repetitions = 2
    factions = Factions(Faction.SPACING_GUILD)
    cost = 3
    agent_icons = AgentIcons(AgentIcon.SPACING_GUILD)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpiceHunter(ImperiumCard):

    name = "spice_hunter"
    repetitions = 2
    factions = Factions(Faction.FREMEN)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.FREMEN, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class SpiceSmugglers(ImperiumCard):

    name = "spice_smugglers"
    repetitions = 2
    factions = Factions(Faction.SPACING_GUILD)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.CITY)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class Stilgar(ImperiumCard):

    name = "stilgar"
    factions = Factions(Faction.FREMEN)
    cost = 5
    agent_icons = AgentIcons(AgentIcon.FREMEN, AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int): ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TesteOfHumanity(ImperiumCard):

    name = "test_of_humanity"
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 3
    agent_icons = AgentIcons(
        AgentIcon.BENE_GESSERIT, AgentIcon.LANDSRAAT, AgentIcon.CITY
    )

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class TheVoice(ImperiumCard):

    name = "the_voice"
    repetitions = 2
    factions = Factions(Faction.BENE_GESSERIT)
    cost = 2
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ThufirHawat(ImperiumCard):

    name = "thufir_hawat"
    cost = 5
    agent_icons = AgentIcons(
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.BENE_GESSERIT,
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    )

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class WormRiders(ImperiumCard):

    name = "worm_riders"
    repetitions = 2
    factions = Factions(Faction.FREMEN)
    cost = 6
    agent_icons = AgentIcons(AgentIcon.CITY, AgentIcon.SPICE_TRADE)

    def play_as_agent(self, player_id: int) -> None: ...

    def play_as_revelation(self, player_id: int) -> None: ...


class ImperiumDeck:

    cards: list[ImperiumCard]

    def initialize(self):
        self.cards = [
            subclass()
            for subclass in ImperiumCard.__subclasses__()
            for _ in range(subclass.repetitions)
        ]
        shuffle(self.cards)
