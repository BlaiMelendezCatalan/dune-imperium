from fastapi import APIRouter

from dune_imperium.game import Game
from dune_imperium.server.dependencies import CrudDependency


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/game", tags=["game"])

    @router.post("/{game_name}/new_game/")
    def new_game(): ...

    @router.post("/{game_name}/add_player/")
    def add_player(): ...

    @router.post("/{game_name}/start_game/")
    async def start_game(
        crud: CrudDependency,
        game_name: str,
    ):
        game = await crud.get_game(game_name)
        if game is None:
            game = Game(name=game_name)  # TODO still need to manage players
            game.round_start()
            await crud.add_game(game)
            # TODO set game state in UI
        else:
            # TODO set game state in UI
            ...

    @router.post("/{game_name}/play_card_as_agent/")
    def play_card_as_agent(
        crud: CrudDependency,
        game_name: str,
    ):
        # Request content includes player_id, card_name, icon_clicked
        # Get game
        # Check that the player has agents
        # Show available locations
        ...

    @router.post("/{game_name}/select_location/")
    def select_location():
        # Request content includes player_id, location name
        # ...
        ...

    return router
