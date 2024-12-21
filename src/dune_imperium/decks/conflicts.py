from abc import ABC, abstractmethod


class ConflictCard(ABC):

    @abstractmethod
    def execute_first_prize(self, player_name: str) -> None:
        pass

    @abstractmethod
    def execute_second_prize(self, player_name: str) -> None:
        pass

    @abstractmethod
    def execute_third_prize(self, player_name: str) -> None:
        pass
