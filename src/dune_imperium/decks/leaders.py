class Leader:

    name: str

    def base_ability(self, player_id: int) -> None:
        # TODO call to API with player_id and leader name
        ...

    def signet_ability(self, player_id: int) -> None:
        # TODO call to API with player_id and leader name
        ...


class BaronVladimirHarkonnen(Leader):

    name = "baron_vladimir_harkonnen"


class CountessArianaThorvald(Leader):

    name = "countess_ariana_thorvald"


class CountIlbanRichese(Leader):

    name = "count_ilban_richese"


class CountMemnonThorvald(Leader):

    name = "count_memnon_throvald"


class DukeaLetoAtreides(Leader):

    name = "duke_leto_atreides"


class GlossuRabban(Leader):

    name = "glossu_rabban"


class HelenaRichese(Leader):

    name = "helena_richese"


class PaulAtreides(Leader):

    name = "paul_atraides"


class LeaderDeck:

    leaders: list[Leader]

    def initialize(self) -> None:
        self.leaders = [subclass() for subclass in Leader.__subclasses__()]
