from pydantic import BaseModel


class Control(BaseModel):

    def add_troop(self) -> None:
        # Implement here
        pass


class SolariControl(Control):

    def add_resource(self):
        # TODO call API to add solari resource to player with player_id
        ...


class SpiceControl(Control):

    def add_resource(self):
        # TODO call API to add spice resource to player with player_id
        ...
