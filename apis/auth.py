from datetime import datetime
from flask import Blueprint, request
from database.users import getUser, add_user
import bcrypt
from utils.auth import hash_password

auth = Blueprint('auth', __name__)
auth.url_prefix = '/auth'

@auth.route('/signup', methods=["POST"])
def create_user():
    data = request.json
    email = data.get("email")
    if getUser(email) == None:
        firstname = data.get("firstname")
        lastname = data.get("lastname")
        password = str(data.get("password"))
        salt = bcrypt.gensalt()
        hashedPassword = hash_password(password, salt)
        add_user(firstname, lastname, email, hashedPassword, "form", salt,datetime.now())
    return "Singed up Successfully"