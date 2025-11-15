import uuid

from fastapi import APIRouter

from dune_imperium.game import Game
from dune_imperium.server.dependencies import CrudDependency


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/games", tags=["game"])

    @router.post("/{game_name}/create_game")
    async def create_game(game_name: str, crud: CrudDependency):
        game_id = str(uuid.uuid4()).replace("-", "")
        game = Game(id=game_id, name=game_name)
        # Expose first 5 imperium cards
        [game.exposed_imperium_deck.add(game.imperium_deck.pop()) for _ in range(5)]
        # Set first player as current player
        game.current_player = game.first_player
        await crud.create_game(game)
        return game_id

    @router.get("/{game_id}")
    async def read_game(game_id: str, crud: CrudDependency):
        return await crud.read_game(game_id)

    @router.get("/")
    async def list_games(crud: CrudDependency):
        return await crud.list_games()

    @router.patch("/update_game")
    async def update_game(crud: CrudDependency, game: Game):
        return await crud.update_game(game)

    @router.delete("/{game_id}")
    async def delete_game(game_id: str, crud: CrudDependency):
        return await crud.delete_game(game_id)

    # TODO implement influence and alliances end points

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
