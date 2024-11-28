from flask import Blueprint, request, jsonify

from app.repository.insert_repository import insert_data

phone_blueprint = Blueprint('phones', __name__)

@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   try:
      data = request.json
      res = insert_data(data)
      print(res if res is not None else 'one sided interaction!, we will pass this one')
      return jsonify({}), 200
   except Exception as e:
      print(e)
      return jsonify({'error': str(e)}), 400