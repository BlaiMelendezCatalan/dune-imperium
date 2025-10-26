from asyncio import Lock
from typing import Annotated, Any

from fastapi import Depends

from dune_imperium.server.crud import Crud

_lock: dict[str, Any] = {"general": Lock()}


def get_lock() -> dict[str, Any]:
    return _lock


async def get_crud(lock: Annotated[dict[str, Any], Depends(get_lock)]) -> Crud:
    crud = Crud(lock)
    await crud.initialize_database()
    return crud


CrudDependency = Annotated[Crud, Depends(get_crud)]
