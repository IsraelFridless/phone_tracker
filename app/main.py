from flask import Flask

from app.routes.device_routes import device_blueprint
from app.routes.interaction_routes import interaction_blueprint
from app.routes.phone_tracker_route import phone_tracker_blueprint

app = Flask(__name__)

app.register_blueprint(phone_tracker_blueprint, url_prefix='/api/phone_tracker')
app.register_blueprint(device_blueprint, url_prefix='/api/devices')
app.register_blueprint(interaction_blueprint, url_prefix='/api/interactions')

if __name__ == '__main__':
    app.run(port=5000)