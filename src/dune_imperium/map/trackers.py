# TODO agent -> location -> reward -> call to API -> player -> tracker -> increase + call to API manage logic
class InfluenceTracker:

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


# TODO agent -> location -> reward -> call to API -> player -> tracker -> increase + call to API if winning?
class VictoryPointsTracker:

    def __init__(self, initial_victory_points: int) -> None:
        self._victory_points = initial_victory_points

    def increase_victory_points(self, player_id: int) -> None:
        # TODO call API if VP goal is reached
        pass

    def decrease_victory_points(self, player_id: int) -> None:
        # TODO call API with influence tracker name to decrease the influence and manage all logic implied
        # rewards, influence points, aliance markers.
        pass

    @property
    def victory_points(self) -> int:
        return self._victory_points
