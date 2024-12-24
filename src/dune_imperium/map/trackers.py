from pydantic import BaseModel


class InfluenceTracker(BaseModel):

    influence: int = 0
    max_influence: int = 6

    def increase_influence(self, player_id: int) -> None:
        # TODO call API with influence tracker name to increase the influence and manage all logic implied:
        # rewards, influence points, aliance markers.
        pass

    def decrease_influence(self, player_id: int) -> None:
        # TODO call API with influence tracker name to decrease the influence and manage all logic implied
        # rewards, influence points, aliance markers.
        pass
