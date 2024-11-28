from flask import Blueprint, jsonify, request

from app.repository.interaction_repository import is_devices_connected, get_most_recent_interaction

interaction_blueprint = Blueprint('interactions', __name__)


@interaction_blueprint.route("/is_devices_connected", methods=['GET'])
def is_devices_connected_route():
   try:
       device_id_1 = request.args.get('device_id_1')
       device_id_2 = request.args.get('device_id_2')
       is_connected = is_devices_connected(device_id_1, device_id_2).value_or(False)
       return jsonify({'is_connected': is_connected}), 200
   except Exception as e:
       return jsonify({'error': str(e)})


@interaction_blueprint.route("/most_recent_interaction/<string:device_id>", methods=['GET'])
def get_most_recent_interaction_route(device_id: str):
   try:
       most_recent_interaction = get_most_recent_interaction(device_id)
       return jsonify({'most_recent_interaction': most_recent_interaction.value_or({})}), 200
   except Exception as e:
       return jsonify({'error': str(e)})