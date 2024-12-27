from asyncio import Lock
from fastapi import Depends
from typing import Annotated, Any

from dune_imperium.server.crud import Crud


_lock: dict[str, Any] = {"general": Lock(), "games": {}}


def get_lock() -> dict[str, Any]:
    return _lock


def get_crud(lock: Annotated[dict[str, Any], Depends(get_lock)]) -> Crud:

    return Crud(lock)


CrudDependency = Annotated[Crud, Depends(get_crud)]
