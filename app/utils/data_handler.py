from datetime import datetime

from app.db.models import Device
from app.db.models.interaction import Interaction
from app.db.models.location import Location


def convert_to_device(device_dict: dict) -> Device:
    location_dict = device_dict['location']
    return Device(
        id=device_dict['id'],
        brand=device_dict['brand'],
        model=device_dict['model'],
        os=device_dict['os'],
        location=convert_do_location(location_dict)
    )

def convert_do_location(location_dict: dict) -> Location:
    return Location(
        latitude=location_dict['latitude'],
        longitude=location_dict['longitude'],
        altitude_meters=location_dict['altitude_meters'],
        accuracy_meters=location_dict['accuracy_meters']
    )

def convert_to_interaction(interaction: dict) -> Interaction:
    return Interaction(
        from_device=interaction['from_device'],
        to_device=interaction['to_device'],
        method=interaction['method'],
        bluetooth_version=interaction['bluetooth_version'],
        signal_strength_dbm=interaction['signal_strength_dbm'],
        distance_meters=interaction['distance_meters'],
        duration_seconds=interaction['duration_seconds'],
        timestamp=datetime.strptime(interaction['timestamp'], '%Y-%m-%dT%H:%M:%S')
    )