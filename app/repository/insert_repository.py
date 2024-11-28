from typing import List, Dict, Optional

from app.db.database import driver
from app.db.models import Device
from app.db.models.interaction import Interaction
from app.repository.queries import insert_device_query, create_interaction_relation_query
from app.utils.data_handler import convert_to_device, convert_to_interaction



def insert_data(data: Dict) -> Optional[List[Dict]]:
    device_1: Device = convert_to_device(data['devices'][0])
    device_2: Device = convert_to_device(data['devices'][1])
    interaction: Interaction = convert_to_interaction(data['interaction'])

    if interaction.from_device == interaction.to_device:
        return

    with driver.session() as session:
        device_1_query, device_1_params = insert_device_query(device_1)
        device_2_query, device_2_params = insert_device_query(device_2)
        interaction_query, interaction_params = create_interaction_relation_query(interaction)

        result_1 = session.run(device_1_query, device_1_params)
        result_2 = session.run(device_2_query, device_2_params)
        result_3 = session.run(interaction_query, interaction_params)

        return [result_1.data(), result_2.data(), result_3.data()]