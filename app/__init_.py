from flask_restplus import Api
from flask import Blueprint

from .main.controller.book_controller import api as book_ns
from .main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-Key'
    }
}

api = Api(blueprint,
            authorizations=authorizations,        
            version='1.0',
            doc='/documentation',
            default='RestPlus Boilerplate',
            default_label='Boilerplate Description')

api.add_namespace(book_ns, path='/book')
api.add_namespace(user_ns, path='/user')