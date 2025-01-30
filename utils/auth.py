import bcrypt

def hash_password(password:str, salt:str):
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")