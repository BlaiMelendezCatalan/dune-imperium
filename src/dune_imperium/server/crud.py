from asyncio import Lock
from contextlib import asynccontextmanager
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from typing import Any, AsyncGenerator

from dune_imperium.database.models import Base, GameSQL
from dune_imperium.game import Game


class Crud:

    def __init__(self, lock: dict[str, Any]) -> None:
        self._lock = lock

    async def initialize_database(self) -> None:
        engine = create_async_engine(
            "sqlite+aiosqlite:///./test.db", echo=True
        )  # TODO: put this in some constants.py file
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def _get_session(self, lock_name: str) -> AsyncGenerator[AsyncSession, None]:
        if lock_name not in self._lock:
            self._lock[lock_name] = Lock()
        async with self._lock[lock_name]:
            engine = create_async_engine(
                "sqlite+aiosqlite:///./test.db", echo=True
            )  # TODO: put this in some constants.py file
            async_session = async_sessionmaker(engine, expire_on_commit=False)
            async with async_session.begin() as session:
                yield session

    @staticmethod
    def _to_pydantic(game_sql: GameSQL) -> Game:
        return Game.model_validate(game_sql.state)

    @staticmethod
    def _to_sql(game: Game) -> GameSQL:
        return GameSQL(
            game_id=game.id, name=game.name, state=game.model_dump()
        )  # TODO maybe add state to Game class?

    async def create_game(self, game: Game) -> Game:
        async with self._get_session(lock_name="general") as session:
            game_sql = self._to_sql(game)
            session.add(game_sql)
            return game

    async def read_game(self, game_id: str) -> Game:
        async with self._get_session(lock_name=game_id) as session:
            query = select(GameSQL).where(GameSQL.game_id == game_id)
            result = await session.execute(query)
            game_sql = result.scalar_one()
            return self._to_pydantic(game_sql)

    async def list_games(self) -> list[str]:
        async with self._get_session(lock_name="general") as session:
            query = select(GameSQL)
            result = await session.execute(query)
            games_sql = result.scalars().all()
            return [self._to_pydantic(game_sql).id for game_sql in games_sql]

    async def update_game(self, game: Game) -> None:
        async with self._get_session(lock_name=game.id) as session:
            query = (
                update(GameSQL)
                .where(GameSQL.game_id == game.id)
                .values(state=game.model_dump())
            )
            await session.execute(query)

    async def delete_game(self, game_id) -> None:
        async with self._get_session(lock_name=game_id) as session:
            query = delete(GameSQL).where(GameSQL.game_id == game_id)
            await session.execute(query)
