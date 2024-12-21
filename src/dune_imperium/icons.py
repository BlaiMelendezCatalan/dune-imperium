from enum import Enum


class AgentIcon(Enum):

    EMPEROR = 1
    SPACING_GUILD = 2
    BENE_GESSERIT = 3
    FREMEN = 4
    LANDSRAAT = 5
    CITY = 6
    SPICE_TRADE = 7


class AgentIcons:

    def __init__(self, *icons: AgentIcon) -> None:
        self._icons: list[AgentIcon] = list(icons)

    @property
    def icons(self) -> list[AgentIcon]:
        return self._icons
