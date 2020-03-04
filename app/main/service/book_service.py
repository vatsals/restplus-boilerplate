from app.main import db


def save_new_book(data):
    book_id = db.books.insert(data)
    return {'_id': str(book_id), 'status': True, 'message': 'Book inserted successfully :)'}


def get_all_books():
    books = list(db.books.find({}))
    return books


def get_a_book(bookname):
    book = db.books.find_one({"book": bookname})
    return book
    

def update_book(data):
    book = db.books.update({"book": data['book']}, data)
    return book


def delete_book(book_id):
    book = db.books.remove({"_id": book_id})
    return book