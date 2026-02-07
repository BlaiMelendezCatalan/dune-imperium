from pathlib import Path

from pydantic_settings import BaseSettings


def default_db_path() -> Path:
    base = Path.home() / ".local" / "share" / "dune_imperium"
    return base / "dune.db"


class Settings(BaseSettings):

    dune_db_path: Path = default_db_path()
