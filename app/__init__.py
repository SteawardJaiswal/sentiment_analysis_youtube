from flask import Flask
from .routes import blueprint as main_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    return app
