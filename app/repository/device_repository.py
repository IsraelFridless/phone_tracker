from returns.maybe import Maybe

from app.db.database import driver


def get_devices_with_longest_path():
    with driver.session() as session:
        query = '''
        MATCH (start:Device)
        MATCH (end:Device)
        WHERE start <> end
        MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
        WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
        WITH path, length(path) AS pathLength
        ORDER BY pathLength DESC
        LIMIT 1
        RETURN path, pathLength;
        '''
        res = session.run(query).data()
        return (
            Maybe.from_optional(res)
            .map(lambda record: {
                "path_length": record[0]['pathLength'],
                "nodes": record[0]['path']
            })
        )


def get_devices_with_strong_connection():
    with driver.session() as session:
        query = '''
        MATCH (start:Device)
        MATCH (end:Device)
        WHERE start <> end
        MATCH path = shortestPath((start)-[:CONNECTED*]->(end))
        WHERE ALL(r IN relationships(path) WHERE r.signal_strength_dbm > -60)
        WITH path, length(path) AS pathLength
        ORDER BY pathLength DESC
        LIMIT 1
        RETURN path, pathLength;
        '''
        res = session.run(query).data()
        return (
            Maybe.from_optional(res)
            .map(lambda record: {
                "path_length": record[0]['pathLength'],
                "nodes": record[0]['path']
            })
        )


def get_count_devices_connected_by_device(device_id: str):
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