from fastapi import APIRouter
from pydantic import BaseModel

from dune_imperium.decks.base import BaseBigCard
from dune_imperium.server.dependencies import CrudDependency


def make_routes() -> APIRouter:

    router = APIRouter(prefix="/action", tags=["actions"])

    class Request(BaseModel):
        game_id: str
        player_id: int

    @router.post("/draw_cards/{num_cards}")
    async def draw_cards(
        num_cards: int, crud: CrudDependency, request: Request
    ) -> None:
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        drawn_cards = 0
        try:
            for _ in range(num_cards):
                player.hand.add(player.source_deck.pop())
                drawn_cards += 1
        except IndexError:
            player.source_deck.rebuild(player.discard_pile.cards)
            player.discard_pile.card_dict = {}
            for _ in range(num_cards - drawn_cards):
                player.hand.add(player.source_deck.pop())
        await crud.update_game(game)

    @router.post("/acquire_card/{card_name}")
    async def acquire_card(
        crud: CrudDependency, card_name: str, request: Request
    ) -> None:
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        player.discard_pile.add(game.pop_exposed_card(card_name))
        game.exposed_imperium_deck.add(game.imperium_deck.pop())
        await crud.update_game(game)

    @router.post("/agent_turn/{card_name}/{location_name}")
    async def agent_turn(
        card_name: str, location_name: str, crud: CrudDependency, request: Request
    ):
        # TODO this should also receive location_name, and then:
        # 1. check that the player has an available agent
        # 2. check that the location is not full
        # 3. deploy the agent to that location paying any costs
        # 4. get agent reward
        # 5. get location reward
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        card: BaseBigCard = player.hand.pop(card_name)
        player.in_play.add(card)
        card.agent_reward(player)
        await crud.update_game(game)

    @router.post("/reveal_turn")
    async def reveal_turn(crud: CrudDependency, request: Request):
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        while player.hand.cards:
            card: BaseBigCard = player.hand.pop()
            card.revelation_reward(player)
            player.in_play.add(card)
        while player.in_play.cards:
            player.discard_pile.add(player.in_play.pop())
        await crud.update_game(game)

    @router.post("/trash_card/{card_name}/{source}")
    async def trash_card(
        crud: CrudDependency, card_name: str, source: str, request: Request
    ) -> None:
        game = await crud.read_game(request.game_id)
        player = game.players[request.player_id]
        # TODO reserve cards return to their decks when trashed
        if source == "hand":
            card = player.hand.pop(card_name)
        elif source == "in_play":
            card = player.in_play.pop(card_name)
        elif source == "discard_pile":
            card = player.discard_pile.pop(card_name)
        else:
            raise ValueError(f"You cannot trash cards from {source}.")
        game.trashed_big_card_deck.add([card])
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
