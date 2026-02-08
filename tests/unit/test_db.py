from asyncio import Lock
from pathlib import Path
from typing import Any
import uuid
import pytest
import pytest_asyncio
import sqlalchemy

from dune_imperium.decks.leaders import CountessArianaThorvald, GlossuRabban, PaulAtreides
from dune_imperium.game import Game
from dune_imperium.player import Player
from dune_imperium.server.crud import Crud


@pytest_asyncio.fixture
async def crud(tmp_path: Path) -> Crud:
    lock: dict[str, Any] = {"general": Lock()}
    db_path = tmp_path / f"test-{uuid.uuid4()}.db"
    crud = Crud(lock, db_path)
    await crud.initialize_database()
    return crud


@pytest.fixture
def game() -> Game:
    players: dict[int, Player] = {
        0: Player(id=0, leader=PaulAtreides()),
        1: Player(id=1, leader=GlossuRabban()),
        2: Player(id=2, leader=CountessArianaThorvald()),
    }
    return Game(id="id", name="name", players=players)


@pytest.fixture
async def loaded_game(game: Game, crud: Crud) -> Game:
    await crud.create_game(game)
    return await crud.read_game(game.id)


@pytest.mark.asyncio
async def test_game_can_be_created(game: Game, crud: Crud):
    await crud.create_game(game)
    assert crud._db_path.is_file()


@pytest.mark.asyncio
async def test_game_can_be_loaded(game: Game, crud: Crud):
    await crud.create_game(game)
    loaded_game = await crud.read_game(game.id)
    for key in game.model_fields:
        assert getattr(loaded_game, key) == getattr(game, key)
    assert loaded_game == game


@pytest.mark.asyncio
async def test_game_can_be_updated(loaded_game: Game, crud: Crud):
    loaded_game.name = "New Name"
    await crud.update_game(loaded_game)
    updated_game = await crud.read_game(loaded_game.id)
    assert updated_game.name == "New Name"


@pytest.mark.asyncio
async def test_games_can_be_listed(loaded_game: Game, crud: Crud):
    new_game = loaded_game.model_copy(update={"id": "id2"}, deep=True)
    await crud.create_game(new_game)
    games = await crud.list_games()
    assert len(games) == 2
    assert games[0] == loaded_game.id
    assert games[1] == new_game.id


@pytest.mark.asyncio
async def test_game_can_be_deleted(loaded_game: Game, crud: Crud):
    await crud.delete_game(loaded_game.id)
    with pytest.raises(sqlalchemy.exc.NoResultFound):
        await crud.read_game(loaded_game.id)
    games = await crud.list_games()
    assert not games