from random import shuffle
from pydantic import BaseModel


class Leader(BaseModel):

    name: str

    def base_ability(self, player_id: int) -> None:
        # TODO call to API with player_id and leader name
        ...

    def signet_ability(self, player_id: int) -> None:
        # TODO call to API with player_id and leader name
        ...


class BaronVladimirHarkonnen(Leader):

    name: str = "baron_vladimir_harkonnen"


class CountessArianaThorvald(Leader):

    name: str = "countess_ariana_thorvald"


class CountIlbanRichese(Leader):

    name: str = "count_ilban_richese"


class CountMemnonThorvald(Leader):

    name: str = "count_memnon_throvald"


class DukeaLetoAtreides(Leader):

    name: str = "duke_leto_atreides"


class GlossuRabban(Leader):

    name: str = "glossu_rabban"


class HelenaRichese(Leader):

    name: str = "helena_richese"


class PaulAtreides(Leader):

    name: str = "paul_atraides"


class LeaderDeck(BaseModel):

    leaders: list[Leader] = []

    def initialize(self) -> None:
        self.leaders = [
            subclass()  # pyright: ignore[reportCallIssue]
            for subclass in Leader.__subclasses__()
        ]
        shuffle(self.leaders)
