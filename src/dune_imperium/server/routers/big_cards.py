from fastapi import APIRouter
from pydantic import BaseModel

from dune_imperium.server.dependencies import CrudDependency


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/cards", tags=["imperium_cards"])

    class Request(BaseModel):
        game_id: str
        player_id: int

    @router.post("/acquire_card/{card_name}")
    async def acquire_card(
        crud: CrudDependency, card_name: str, request: Request
    ) -> None:
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        card = game.exposed_imperium_deck.pop(card_name)
        player.discard_pile.add(card)
        game.expose_n_imperium_cards(n=1)  # TODO: See if this is convenient
        await crud.update_game(game)

    @router.post("/trash_card/{card_name}/{source}")
    async def trash_card(
        crud: CrudDependency, card_name: str, source: str, request: Request
    ) -> None:
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        if source == "hand":
            card = player.hand.cards.pop(card_name)
        elif source == "in_play":
            card = player.in_play.cards.pop(card_name)
        elif source == "discard_pile":
            card = player.discard_pile.cards.pop(card_name)
        else:
            raise ValueError(f"You cannot trash cards from {source}.")
        game.trashed_big_card_deck.add([card])
        await crud.update_game(game)

    @router.post("/play_card/{card_name}/{play_type}")
    async def play_card(
        card_name: str, play_type: str, crud: CrudDependency, request: Request
    ):
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        card = player.hand.cards.pop(card_name)
        player.in_play.add(card)
        if play_type == "agent":
            card.agent_reward(player.id)
        elif play_type == "revelation":
            card.revelation_reward(player.id)
        await crud.update_game(game)

    # @router.post("/{game_id}/arrakis_recruiter/agent_reward")
    # async def arrakis_recruiter_agent_reward(
    #     crud: CrudDependency, game_id: str, request: CardRequest
    # ):
    #     # TODO create a context manager that gets game, checks player is current,
    #     # checks card has not been played, yields game, and updates game
    #     game = await crud.read_game(game_id)
    #     player = game.players[request.player_id]
    #     if player.id != game.current_player:
    #         # TODO tell the user "it is not your turn"
    #         return
    #     card_name = request.card_name
    #     if card_name in player.in_play.cards:
    #         # TODO tell the user this card was already played
    #         return
    #     if not any([agent.deployed for agent in player.agents]):
    #         # TODO tell the user there are no more agents ¿in an HTTPResponse?
    #         return
    #     supply_troops = [
    #         troop for troop in player.troops if troop.state == TroopState.SUPPLY
    #     ]
    #     if not supply_troops:
    #         # TODO tell the user there are no more agents ¿in an HTTPResponse?
    #         return
    #     supply_troops[0].state = TroopState.GARRISON
    #     if card := player.hand.cards.get(card_name):
    #         player.in_play.add(card)
    #     else:
    #         # Tell the user
    #         ...
    #     await crud.update_game(game)

    # @router.post("/{game_name}/arrakis_recruiter/revelation_reward")
    # async def arrakis_recruiter_reveal_reward(
    #     crud: CrudDependency, game_name: str, request: CardRequest
    # ):
    #     # game = await crud.get_game(game_name)
    #     # player_id = request.player_id
    #     # player = game.players[player_id]
    #     # TODO reward
    #     ...

    return router
