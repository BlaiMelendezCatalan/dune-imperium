from typing import TYPE_CHECKING, Self

from pydantic import BaseModel

from dune_imperium.agent_icons.icons import AgentIcon
from dune_imperium.decks.base import BaseBigCard, BaseSourceDeck
from dune_imperium.decks.factions import Faction

if TYPE_CHECKING:
    from dune_imperium.player import Player


class ImperiumCard(BaseBigCard): ...


class ArrakisRecruiter(ImperiumCard):

    name: str = "arrakis_recruiter"
    repetitions: int = 2
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 1


class AssassinationMission(ImperiumCard):

    name: str = "assassination_mission"
    repetitions: int = 2
    persuasion_cost: int = 1

    def revelation_reward(self, player: "Player") -> None:
        player.resources.solari += 1
        player.swords += 1


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

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class BeneGesseritSister(ImperiumCard):

    name: str = "bene_gesserit_sister"
    repetitions: int = 3
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.LANDSRAAT]

    def revelation_reward(self, player: "Player") -> None:
        # TODO 2 persuasion or 2 swords -> requires player choice
        ...


class Carryall(ImperiumCard):

    name: str = "carryall"
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.resources.spice += 1


class Chani(ImperiumCard):

    name: str = "chani"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2
        # TODO retreat any number of troops from a battle -> requires player choice


class ChoamDirectorship(ImperiumCard):

    name: str = "choam_directorship"
    persuasion_cost: int = 8

    def revelation_reward(self, player: "Player") -> None:
        player.resources.solari += 3


class Crysknife(ImperiumCard):

    name: str = "crysknife"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.swords += 1
        # TODO fremen bond


class DoctorYueh(ImperiumCard):

    name: str = "doctor_yueh"
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class DuncanIdaho(ImperiumCard):

    name: str = "duncan_idaho"
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.swords += 2
        player.resources.water += 1


class FedaykinDeathCommando(ImperiumCard):

    name: str = "fedaykin_death_commando"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        # TODO fremen bond


class FirmGrip(ImperiumCard):

    name: str = "firm_grip"
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]

    def revelation_reward(self, player: "Player") -> None:
        # TODO needs implementation of aliance markers and refactor of influence trackers?
        # We can call endpoints to modify game state from here
        ...


class FremenCamp(ImperiumCard):

    name: str = "fremen_camp"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2
        player.swords += 1


class GeneManipulation(ImperiumCard):

    name: str = "gene_manipulation"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class GuildAdministrator(ImperiumCard):

    name: str = "guild_administrator"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class GuildAmbassador(ImperiumCard):

    name: str = "guild_ambassador"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT]

    def revelation_reward(self, player: "Player") -> None:
        # TODO needs implementation of aliance markers and refactor of influence trackers?
        ...


class GuildBankers(ImperiumCard):

    name: str = "guild_bankers"
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.EMPEROR,
        AgentIcon.SPACING_GUILD,
        AgentIcon.LANDSRAAT,
    ]

    def revelation_reward(self, player: "Player") -> None:
        # TODO requires more complex logic
        ...


class GunThopter(ImperiumCard):

    name: str = "gun_thopter"
    repetitions: int = 2
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.swords += 3
        # TODO requires more complex logic


class GurneyHalleck(ImperiumCard):

    name: str = "gurney_halleck"
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2
        # TODO requires more complex logic


class ImperialSpy(ImperiumCard):

    name: str = "imperial_spy"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 1


class KwisatzHaderach(ImperiumCard):

    name: str = "kwisatz_haderach"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 8
    agent_icons: list[AgentIcon] = []

    def revelation_reward(self, player: "Player") -> None:
        card = player.source_deck.pop()
        player.hand.add(card)
        # TODO requires more complex logic


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

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 3
        player.swords += 1


class LietKynes(ImperiumCard):

    name: str = "liet_kynes"
    factions: list[Faction] = [Faction.EMPEROR, Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        for card in player.in_play.cards:
            if Faction.FREMEN in card.factions:
                player.persuasion += 2


class MissionariaProtectiva(ImperiumCard):

    name: str = "missionaria_protectiva"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1


class Opulence(ImperiumCard):

    name: str = "opulence"
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        # TODO requires more complex logic


class OtherMemory(ImperiumCard):

    name: str = "other_memory"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class PiterDeVries(ImperiumCard):

    name: str = "piter_de_vries"
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 3
        player.swords += 1


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


class ReverendMotherMohiam(ImperiumCard):

    name: str = "reverend_mother_mohiam"
    factions: list[Faction] = [Faction.EMPEROR, Faction.BENE_GESSERIT]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.BENE_GESSERIT]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2
        player.resources.spice += 2


class SardaukarInfantry(ImperiumCard):

    name: str = "sardaukar_infantry"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = []

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 2


class SardaukarLegion(ImperiumCard):

    name: str = "sardaukar_legion"
    repetitions: int = 2
    factions: list[Faction] = [Faction.EMPEROR]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [AgentIcon.EMPEROR, AgentIcon.LANDSRAAT]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        # TODO requires more complex logic


class Scout(ImperiumCard):

    name: str = "scout"
    repetitions: int = 2
    persuasion_cost: int = 1
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 1
        # TODO requires more complex logic


class ShiftingAllegiances(ImperiumCard):

    name: str = "shifting_allegiances"
    repetitions: int = 2
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.LANDSRAAT, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class SietchReverendMother(ImperiumCard):

    name: str = "sietch_reverend_mother"
    factions: list[Faction] = [Faction.BENE_GESSERIT, Faction.FREMEN]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.BENE_GESSERIT, AgentIcon.FREMEN]

    def revelation_reward(self, player: "Player") -> None:
        # TODO fremen bond
        ...


class SmugglersThopter(ImperiumCard):

    name: str = "smugglers_thopter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 4
    agent_icons: list[AgentIcon] = [AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.resources.spice += 1


class SpaceTravel(ImperiumCard):

    name: str = "space_travel"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [AgentIcon.SPACING_GUILD]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class SpiceHunter(ImperiumCard):

    name: str = "spice_hunter"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.FREMEN, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 1
        # TODO fremen bond


class SpiceSmugglers(ImperiumCard):

    name: str = "spice_smugglers"
    repetitions: int = 2
    factions: list[Faction] = [Faction.SPACING_GUILD]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        player.swords += 1


class Stilgar(ImperiumCard):

    name: str = "stilgar"
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 5
    agent_icons: list[AgentIcon] = [
        AgentIcon.FREMEN,
        AgentIcon.CITY,
        AgentIcon.SPICE_TRADE,
    ]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2
        player.swords += 3


class TestOfHumanity(ImperiumCard):

    name: str = "test_of_humanity"
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 3
    agent_icons: list[AgentIcon] = [
        AgentIcon.BENE_GESSERIT,
        AgentIcon.LANDSRAAT,
        AgentIcon.CITY,
    ]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


class TheVoice(ImperiumCard):

    name: str = "the_voice"
    repetitions: int = 2
    factions: list[Faction] = [Faction.BENE_GESSERIT]
    persuasion_cost: int = 2
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 2


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

    def revelation_reward(self, player: "Player") -> None:
        player.persuasion += 1
        # TODO requires call to draw intrigue endpoint


class WormRiders(ImperiumCard):

    name: str = "worm_riders"
    repetitions: int = 2
    factions: list[Faction] = [Faction.FREMEN]
    persuasion_cost: int = 6
    agent_icons: list[AgentIcon] = [AgentIcon.CITY, AgentIcon.SPICE_TRADE]

    def revelation_reward(self, player: "Player") -> None:
        if player.fremen_influence.influence >= 1:
            player.swords += 4
        # TODO allieance marker logic


class ImperiumDeck(BaseSourceDeck[ImperiumCard]):

    def initialize(self) -> Self:
        super()._initialize(ImperiumCard)
        return self


class ExposedImperiumDeck(BaseModel):

    cards: dict[str, ImperiumCard] = {}

    def add(self, card: ImperiumCard):
        self.cards.update({card.name: card})

    def pop(self, card_name: str) -> ImperiumCard:
        return self.cards.pop(card_name)
