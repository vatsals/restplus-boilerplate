from flask import request
from flask_restplus import Resource, reqparse
from bson import ObjectId

from ..util.dto import BookDto
from ..util.decorator import token_required
from ..service.book_service import save_new_book, get_all_books, get_a_book, update_book, delete_book

api = BookDto.api
_book = BookDto.book_schema

book_parser = reqparse.RequestParser()
book_parser.add_argument('book_id', type=str, required=True)


@api.route('/')
class BookList(Resource):
    @api.doc('List of Books', security='apikey')
    @token_required
    @api.marshal_list_with(_book, envelope='result')
    def get(self):
        return get_all_books()

    @api.expect(_book, validate=True)
    @api.response(201, 'Book Added')
    @api.doc('Create a new Book', security='apikey')
    def post(self):
        data = request.json
        return save_new_book(data=data)

    @api.expect(_book, validate=True)
    @api.response(201, 'Book Updated')
    @api.doc('Update a new Book', security='apikey')
    def put(self):
        data = request.json
        return update_book(data=data)

    @api.response(201, 'Book Deleted')
    @api.doc(parser=book_parser, response={200: 'OK', 500: 'Internal Server Error'}, security='apikey')
    def delete(self):
        args = book_parser.parse_args()
        return delete_book(ObjectId(args['book_id']))


@api.route('/<bookname>')
@api.param('bookname', 'Book Name')
@api.response(404, 'Book not found')
class Book(Resource):
    @api.doc('Get a book')
    @api.marshal_with(_book)
    def get(self, bookname):
        book = get_a_book(bookname)
        return api.abort(404) if not book else book