from pydantic import BaseModel, Field


class Game(BaseModel):

    name: str = Field(pattern=r"^[A-Za-z0-9_]{1,25}$")

    max_players: int
    player_names: dict[int, str] = {}
