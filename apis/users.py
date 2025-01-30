from flask import Blueprint
from database.users import getUsers

users = Blueprint('users', __name__)
users.url_prefix = '/users'

@users.route('/')
def get_users():
    return getUsers()