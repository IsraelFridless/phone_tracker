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