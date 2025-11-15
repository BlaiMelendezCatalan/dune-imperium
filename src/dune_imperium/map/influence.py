from typing import TYPE_CHECKING

from pydantic import BaseModel

from dune_imperium.factions.factions import Faction

if TYPE_CHECKING:
    from dune_imperium.game import Game
    from dune_imperium.player import Player


MAX_INFLUENCE = 6


class InfluenceTracker(BaseModel):

    influence: dict[int, int] = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
    }
    faction: Faction

    def increase_influence(self, player: "Player", game: "Game") -> None:
        self.influence[player.id] = min(MAX_INFLUENCE, self.influence[player.id] + 1)
        if self.influence[player.id] == 2:
            player.victory_points += 1
        if self.influence[player.id] == 4:
            match self.faction:
                case Faction.FREMEN:
                    player.resources.water += 1
                case Faction.BENE_GESSERIT:
                    intrigue_card = game.intrigue_deck.pop()
                    player.intrigues.add(intrigue_card)
                case Faction.SPACING_GUILD:
                    player.resources.solari += 3
                case Faction.EMPEROR:
                    player.troops.recruit(2)
        if (
            self._get_leading_players_id() == [player.id]
            and self.influence[player.id] >= 4
        ):
            former_player_id = game.alliance_tracker[self.faction]
            if former_player_id and former_player_id == player.id:
                return
            elif not former_player_id or former_player_id != player.id:
                game.alliance_tracker[self.faction] = player.id
                player.victory_points += 1
                if former_player_id:
                    former_player = game.players[former_player_id]
                    former_player.victory_points -= 1

    def decrease_influence(self, player: "Player", game: "Game") -> None:
        self.influence[player.id] = max(0, self.influence[player.id] - 1)
        if self.influence[player.id] == 1:
            player.victory_points -= 1
        if player.id not in self._get_leading_players_id():
            # TODO think about alliance removal
            ...

    def _get_leading_players_id(self) -> list[int]:
        max_influence = max(self.influence.values())
        leading_players = [
            player_id
            for player_id, influence in self.influence.items()
            if influence == max_influence
        ]
        return leading_players
