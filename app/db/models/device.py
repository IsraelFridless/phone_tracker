from dataclasses import dataclass

from app.db.models.location import Location


@dataclass
class Device:
    id: str
    brand: str
    model: int
    os: str
    location: Location