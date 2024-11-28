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
            Maybe.from_optional(res.get('exists'))
        )