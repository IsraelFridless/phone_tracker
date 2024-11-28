from returns.maybe import Maybe

from app.db.database import driver


def is_devices_connected(device_id_1: str, device_id_2: str, ):
    with driver.session() as session:
        query = '''
        MATCH (d:Device) -[:CONNECTED]-> (d2:Device)
        WHERE d.id = $device_id_1 AND d2.id = $device_id_2
        RETURN COUNT(*) > 0 AS exists;
        '''
        params = {
            'device_id_1': device_id_1,
            'device_id_2': device_id_2
        }
        res = session.run(query, params).single()
        return (
            Maybe.from_optional(res)
            .map(lambda record: record.get('exists'))
        )


def get_most_recent_interaction(device_id: str):
    with driver.session() as session:
        query = '''
        MATCH (d:Device)-[rel:CONNECTED]->(d2:Device)
        WHERE d.id = $device_id
        RETURN rel
        ORDER BY rel.timestamp DESC
        LIMIT 1;
        '''
        res = session.run(query, {'device_id': device_id}).single()

        return (
            Maybe.from_optional(res)
            .map(lambda record: record.get('rel'))
            .map(lambda rel: dict(rel))
            .map(lambda rel: {
                **rel,
                'timestamp': rel['timestamp'].strftime('%Y-%m-%dT%H:%M:%S')
            })
        )