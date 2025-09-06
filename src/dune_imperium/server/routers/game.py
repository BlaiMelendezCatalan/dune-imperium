import uuid
from fastapi import APIRouter

from dune_imperium.game import Game
from dune_imperium.server.dependencies import CrudDependency


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/game", tags=["game"])

    @router.post("/{game_name}/new_game/")
    async def new_game(game_name: str, crud: CrudDependency):
        game_id = str(uuid.uuid4())
        game = Game(id=game_id, name=game_name)
        await crud.add_game(game)

    @router.get("/{game_id}")
    async def get_game(game_id: str, crud: CrudDependency):
        return await crud.get_game(game_id)

    # @router.post("/{game_id}/add_player/")
    # async def add_player(): ...

    # @router.post("/{game_id}/start_game/")
    # async def start_game(
    #     crud: CrudDependency,
    #     game_id: str,
    # ):
    #     game = Game(name=game_id)  # TODO still need to manage players
    #     game.setup()
    #     # TODO render using WebSockets
    #     game.round_start()
    #     # TODO render using WebSockets
    #     await crud.add_game(game)

    # @router.post("/{game_name}/resume_game")
    # async def resume_game(crud: CrudDependency, game_name: str) -> None:
    #     game = await crud.get_game(game_name)
    #     # TODO game.render_state()

    return router
