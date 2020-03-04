from functools import wraps
from flask import request


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'X-API-Key' in request.headers:
            token = request.headers['X-API-Key']

        if not token:
            return {'message': 'Token is missing'}, 401

        if token != 'mytoken':
            return {'message': 'Invalid token'}, 401

        return f(*args, **kwargs)

    return decorated