from flask_restplus import Namespace, fields


class BookDto:
    api = Namespace('Book', description='Book related operations')
    book_schema = api.model('Book', {
        '_id': fields.String(description='User ID'),
        'book': fields.String(required=True, description='Book Name'),
        'genre': fields.String(required=True, description='Genre of the Book'),
        'authorname': fields.String(description='Author of the Book')
    })


class UserDto:
    api = Namespace('User', description='User related operations')
    user_schema = api.model('User', {
        '_id': fields.String(description='User ID'),
        'name': fields.String(required=True, description='Username'),
        'age': fields.Integer(required=True, description='Age'),
        'country': fields.String(description='Country Name')
    })