from fastapi import APIRouter
from pydantic import BaseModel

from dune_imperium.server.dependencies import CrudDependency
from dune_imperium.tokens.troops import TroopState


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/cards", tags=["imperium_cards"])

    class CardRequest(BaseModel):
        player_id: int
        card_name: str

    @router.post("/{game_name}/acquire")
    async def acquire(
        crud: CrudDependency, game_name: str, request: CardRequest
    ) -> None:
        game = await crud.read_game(game_name)
        game.acquire_exposed_card(
            **request.model_dump()
        )  # This should include reserve cards as well
        game.expose_n_imperium_cards(n=1)
        await crud.update_game(game)

    @router.post("/{game_name}/trash")
    async def trash(crud: CrudDependency, game_name: str, request: CardRequest) -> None:
        # TODO for reserve cards, trashing returns card to reserve
        ...

    # IMPERIUM CARDS

    @router.post("/{game_name}/arrakis_recruiter/agent_reward")
    async def arrakis_recruiter_agent_reward(
        crud: CrudDependency, game_name: str, request: CardRequest
    ):
        # TODO create a context manager that gets game, checks player is current,
        # checks card has not been played, yields game, and updates game
        game = await crud.read_game(game_name)
        player = game.players[request.player_id]
        if player.id != game.current_player:
            # TODO tell the user "it is not your turn"
            return
        card_name = request.card_name
        if card_name in player.in_play.cards:
            # TODO tell the user this card was already played
            return
        if not any([agent.deployed for agent in player.agents]):
            # TODO tell the user there are no more agents ¿in an HTTPResponse?
            return
        supply_troops = [
            troop for troop in player.troops if troop.state == TroopState.SUPPLY
        ]
        if not supply_troops:
            # TODO tell the user there are no more agents ¿in an HTTPResponse?
            return
        supply_troops[0].state = TroopState.GARRISON
        if card := player.hand.cards.get(card_name):
            player.in_play.add(card)
        else:
            # Tell the user
            ...
        await crud.update_game(game)

    @router.post("/{game_name}/arrakis_recruiter/revelation_reward")
    async def arrakis_recruiter_reveal_reward(
        crud: CrudDependency, game_name: str, request: CardRequest
    ):
        # game = await crud.get_game(game_name)
        # player_id = request.player_id
        # player = game.players[player_id]
        # TODO reward
        ...

    return router
