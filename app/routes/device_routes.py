from flask import Blueprint, jsonify

from app.repository.device_repository import get_devices_with_longest_path, get_devices_with_strong_connection, \
    get_count_devices_connected_by_device

device_blueprint = Blueprint('devices', __name__)


@device_blueprint.route("/longest_path_devices", methods=['GET'])
def get_devices_with_longest_path_route():
   try:
       longest_path_devices = get_devices_with_longest_path()
       return jsonify(longest_path_devices.value_or({})), 200
   except Exception as e:
       return jsonify({'error': str(e)})


@device_blueprint.route("/devices_with_strong_connection", methods=['GET'])
def get_devices_with_strong_connection_route():
   try:
       devices_with_strong_connection = get_devices_with_strong_connection()
       return jsonify(devices_with_strong_connection.value_or({})), 200
   except Exception as e:
       return jsonify({'error': str(e)})


@device_blueprint.route("/count_device_connected/<string:device_id>", methods=['GET'])
def get_count_devices_connected_by_device_id_route(device_id: str):
   try:
       count_devices_connected = get_count_devices_connected_by_device(device_id)
       return jsonify(count_devices_connected.value_or({})), 200
   except Exception as e:
       return jsonify({'error': str(e)})