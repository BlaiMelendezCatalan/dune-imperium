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
        engine = create_async_engine("TODO")
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @asynccontextmanager
    async def _get_session(self, lock_name: str) -> AsyncGenerator[AsyncSession, None]:
        async with self._lock[lock_name]:
            engine = create_async_engine("TODO")
            async_session = async_sessionmaker(engine, expire_on_commit=False)
            async with async_session.begin() as session:
                yield session

    @staticmethod
    def _to_pydantic(game_sql: GameSQL) -> Game:
        return Game.model_validate(game_sql.state)

    @staticmethod
    def _to_sql(game: Game) -> GameSQL:
        return GameSQL(state=game.model_dump())

    # async def list_games(self, user_name: str) -> None:
    #     async with self._get_session(lock_name="general") as session:
    #         ...

    async def add_game(self, game: Game) -> None:
        async with self._get_session(lock_name="general") as session:
            game_sql = self._to_sql(game)
            session.add(game_sql)

    async def delete_game(self, game_name) -> None:
        async with self._get_session(lock_name=game_name) as session:
            query = delete(GameSQL).where(GameSQL.name == game_name)
            await session.execute(query)

    async def get_game(self, game_name: str) -> Game:
        async with self._get_session(lock_name=game_name) as session:
            query = select(GameSQL).where(GameSQL.name == game_name)
            result = await session.execute(query)
            game_sql = result.scalar_one()
            return self._to_pydantic(game_sql)

    async def update_game(self, game: Game) -> None:
        async with self._get_session(lock_name=game.name) as session:
            query = (
                update(GameSQL)
                .where(GameSQL.name == game.name)
                .values(state=game.model_dump())
            )
            await session.execute(query)
