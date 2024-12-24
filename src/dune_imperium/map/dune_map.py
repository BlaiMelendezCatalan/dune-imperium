from pydantic import BaseModel

from dune_imperium.map.conflict_zone import ConflictZone
from dune_imperium.map.locations import Locations


class DuneMap(BaseModel):

    locations: Locations = Locations()
    confluct_zone: ConflictZone = ConflictZone()
