from app.db.models import Device
from app.db.models.interaction import Interaction


def insert_device_query(device: Device) -> (str, dict):
    query = '''
        MERGE (d:Device {
            id: $id,
            brand: $brand,
            model: $model,
            os: $os,
            latitude: $latitude,
            longitude: $longitude,
            altitude_meters: $altitude_meters,
            accuracy_meters: $accuracy_meters
        })
        return d
    '''
    params = {
        'id': device.id,
        'brand': device.brand,
        'model': device.model,
        'os': device.os,
        'latitude': device.location.latitude,
        'longitude': device.location.longitude,
        'altitude_meters': device.location.altitude_meters,
        'accuracy_meters': device.location.accuracy_meters
    }
    return query, params


def create_interaction_relation_query(interaction: Interaction) -> (str, dict):
    query = '''
        MATCH (device1:Device {id: $from_device})
        MATCH (device2:Device {id: $to_device})
        CREATE (device1)-[:CONNECTED {
            method: $method,
            bluetooth_version: $bluetooth_version,
            signal_strength_dbm: $signal_strength_dbm,
            distance_meters: $distance_meters,
            duration_seconds: $duration_seconds,
            timestamp: datetime($timestamp)
        }] -> (device2);
        '''
    params = {
        'from_device': interaction.from_device,
        'to_device': interaction.to_device,
        'method': interaction.method,
        'bluetooth_version': interaction.bluetooth_version,
        'signal_strength_dbm': interaction.signal_strength_dbm,
        'distance_meters': interaction.distance_meters,
        'duration_seconds': interaction.duration_seconds,
        'timestamp': interaction.timestamp,
    }
    return query, params