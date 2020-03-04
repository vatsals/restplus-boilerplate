from flask import Flask
from pymongo import MongoClient
from flask_cors import CORS

from .config import config_by_name

client = MongoClient()
db = client.restdb


def create_app(config_name):
    app = Flask(__name__)

    CORS(app, resources={r'/*': {'origins': '*'}})
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config.from_object(config_by_name[config_name])

    return app
