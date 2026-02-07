from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field


class Control(BaseModel):

    def add_troop(self) -> None:
        # Implement here
        pass


class SolariControl(Control):

    name: Literal["solari_control"] = "solari_control"

    def add_resource(self):
        # TODO call API to add solari resource to player with player_id
        ...


class SpiceControl(Control):

    name: Literal["spice_control"] = "spice_control"

    def add_resource(self):
        # TODO call API to add spice resource to player with player_id
        ...


ControlType = (
    Annotated[
        Union[SolariControl, SpiceControl],
        Field(discriminator="name"),
    ]
    | None
)
