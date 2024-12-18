from sqlmodel import (
    SQLModel,
    Field,  # pyright: ignore[reportUnknownVariableType]
    Relationship,
)


class PlayerGameLink(SQLModel, table=True):

    player_id: int | None = Field(
        default=None, foreign_key="player.id", primary_key=True
    )
    game_id: int | None = Field(default=None, foreign_key="game.id", primary_key=True)


class Game(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    max_players: int

    players: list["Player"] = Relationship(
        back_populates="games", link_model=PlayerGameLink
    )


class Player(SQLModel, table=True):

    id: int | None = Field(default=None, primary_key=True)
    name: str

    games: list["Game"] = Relationship(
        back_populates="players", link_model=PlayerGameLink
    )
