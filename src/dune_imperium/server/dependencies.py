from asyncio import Lock
from typing import Annotated, Any

from fastapi import Depends

from dune_imperium.config.settings import Settings
from dune_imperium.server.crud import Crud

_lock: dict[str, Any] = {"general": Lock()}


def get_lock() -> dict[str, Any]:
    return _lock


def get_settings() -> Settings:
    return Settings()


async def get_crud(
    lock: Annotated[dict[str, Any], Depends(get_lock)],
    settings: Annotated[Settings, Depends(get_settings)],
) -> Crud:
    crud = Crud(lock, settings.dune_db_path)
    await crud.initialize_database()
    return crud


CrudDependency = Annotated[Crud, Depends(get_crud)]
