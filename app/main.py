from flask import Flask

from app.routes.device_routes import device_blueprint
from app.routes.phone_tracker_route import phone_blueprint

app = Flask(__name__)

app.register_blueprint(phone_blueprint)
app.register_blueprint(device_blueprint, url_prefix='/api/devices')

if __name__ == '__main__':
    app.run(port=5000)