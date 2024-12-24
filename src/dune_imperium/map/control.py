from abc import ABC, abstractmethod
from pydantic import BaseModel


class Control(BaseModel, ABC):

    def add_troop(self) -> None:
        # Implement here
        pass

    @abstractmethod
    def add_resource(self) -> None:
        pass


class SolariControl(Control):

    def add_resource(self):
        # TODO call API to add solari resource to player with player_id
        ...


class SpiceControl(Control):

    def add_resource(self):
        # TODO call API to add spice resource to player with player_id
        ...
