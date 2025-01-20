from flask import Flask
from flask_restx import Api
from app.routes.scientist_crud import scientist_api
from flask_cors import CORS

def create_app():
    """
        Create the application instance.
        :return: Flask application instance
    """
    app = Flask(__name__)
    CORS(app, resources={r"/scientists/*": {"origins": "*"}})
    app.config.from_pyfile('config.py')  # load the instance config file
    api = Api(app, title="Scientist API", version="1.0", description="API for managing scientists")

    # Register namespaces
    api.add_namespace(scientist_api, path='/scientists')

    return app
