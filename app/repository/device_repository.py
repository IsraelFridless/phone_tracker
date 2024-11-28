from returns.maybe import Maybe

from app.db.database import driver


def get_devices_with_longest_path():
    with driver.session() as session:
        query = '''
        MATCH p = (device1:Device)-[:CONNECTED* {method: 'Bluetooth'}]->(device2:Device)
        WITH device1, last(nodes(p)) AS last_device, length(p) AS path_length
        RETURN device1 AS start_device, last_device AS end_device, path_length
        ORDER BY path_length DESC
        LIMIT 1;
        '''
        res = session.run(query).single()
        return (
            Maybe.from_optional(res)
            .map(lambda record: {
                "path_length": record["path_length"],
                "start_device": dict(record["start_device"]),
                "end_device": dict(record["end_device"])
            })
        )


def get_devices_with_strong_connection():
    with driver.session() as session:
        query = '''
        MATCH (d:Device)-[re:CONNECTED]->(d2:Device)
        WHERE re.signal_strength_dbm > -60
        RETURN d AS device, d2 AS connected_device, re.signal_strength_dbm AS signal_strength;
        '''
        res = session.run(query).data()
        return [
            {
                "device": dict(record["device"]),
                "connected_device": dict(record["connected_device"]),
                "signal_strength": record["signal_strength"]
            }
            for record in res
        ]


def get_count_devices_connected_by_device_id(device_id: str):
    with driver.session() as session:
        query = '''
        MATCH (d:Device) -[:CONNECTED]-> (d2:Device)
        WHERE d.id = $device_id
        RETURN COUNT(d) AS devices_count
        '''
        res = session.run(query, {'device_id': device_id}).single()
        return (
            Maybe.from_optional(res)
            .map(lambda d: dict(d))
        )