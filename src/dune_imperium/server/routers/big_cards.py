from fastapi import APIRouter
from pydantic import BaseModel

from dune_imperium.server.dependencies import CrudDependency
from dune_imperium.tokens.troops import TroopState


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/cards", tags=["imperium_cards"])

    class UseCardRequest(BaseModel):
        player_id: int

    class AcquireCardRequest(BaseModel):
        player_id: int
        card_name: str

    @router.post("/{game_name}/acquire")
    async def expose(
        crud: CrudDependency, game_name: str, request: AcquireCardRequest
    ) -> None:
        game = await crud.get_game(game_name)
        game.move_exposed_imperium_card_to_player_discard_pile(**request.model_dump())
        game.expose_next_imperium_card()
        await crud.update_game(game)

    @router.post("/{game_name}/trash")

    # IMPERIUM CARDS

    @router.post("/{game_name}/arrakis_recruiter/agent_reward")
    async def arrakis_recruiter_agent_reward(
        crud: CrudDependency, game_name: str, request: UseCardRequest
    ):
        game = await crud.get_game(game_name)
        player = game.players[request.player_id]
        if not any([agent.deployed for agent in player.agents]):
            # TODO tell the user there are no more agents ¿in an HTTPResponse?
            ...
        supply_troops = [
            troop for troop in player.troops if troop.state == TroopState.SUPPLY
        ]
        if not supply_troops:
            # TODO tell the user there are no more agents ¿in an HTTPResponse?
            ...
        supply_troops[0].state = TroopState.GARRISON
        await crud.update_game(game)

    @router.post("/{game_name}/arrakis_recruiter/reveal_reward")
    async def arrakis_recruiter_reveal_reward(
        crud: CrudDependency, game_name: str, request: UseCardRequest
    ):
        game = await crud.get_game(game_name)
        player_id = request.player_id
        player = game.players[player_id]
        player.hand.reveal(player_id)  #

    return router
