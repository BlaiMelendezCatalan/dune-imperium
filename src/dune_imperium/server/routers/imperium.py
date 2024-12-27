from fastapi import APIRouter
from pydantic import BaseModel

from dune_imperium.server.dependencies import CrudDependency
from dune_imperium.tokens.troops import TroopState


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/imperium_cards", tags=["imperium_cards"])

    class Request(BaseModel):
        player_id: int

    @router.post("/{game_name}/arrakis_recruiter/agent_reward")
    async def get_agent_reward(crud: CrudDependency, game_name: str, request: Request):
        game = await crud.get_game(game_name)
        player = game.players[request.player_id]
        if not any([agent.deployed for agent in player.agents]):
            # TODO tell the user there are no more agents
            ...
        supply_troops = [
            troop for troop in player.troops if troop.state == TroopState.SUPPLY
        ]
        if not supply_troops:
            # TODO tell the user all troops are already in the garrison/combat
            ...
        supply_troops[0].state = TroopState.GARRISON
        await crud.update_game(game)

    return router
