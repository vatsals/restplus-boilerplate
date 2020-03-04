from app.main import db


def save_new_user(data):
    user = get_a_user(data['name'])
    if user:
        return {'status': False, 'message': 'User already exists :/'}

    user_id = db.users.insert(data)
    return {'_id': str(user_id), 'status': True, 'message': 'User inserted successfully :)'}


def get_all_users():
    users = list(db.users.find({}))
    return users


def get_a_user(username):
    user = db.users.find_one({"name": username})
    return user