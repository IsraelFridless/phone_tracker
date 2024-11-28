from flask import Blueprint, request, jsonify

phone_blueprint = Blueprint('phones', __name__)

@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200