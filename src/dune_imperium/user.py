class User:

    def __init__(self, name: str, password: str):
        self._name = name
        self._password = password

    def get_user_game_names(self) -> list[str]: ...
