from sqlalchemy import text, insert, table, select, column
from database.connection import engine

user_table = table("users", column("id"), column("firstname"), column("lastname"), column("created_at"), column("email"), column("hash"), column("salt"), column("signup_method"))

def getUsers():
    with engine.connect() as conn:
        statement = text("SELECT firstname, lastname, email, created_at from USERS")
        result = conn.execute(statement)
        users = []
        for user in result.all():
            users.append(user._asdict())
        return users
    
def getUser(email):
    with engine.connect() as conn:
        statement = select(user_table.c.firstname, user_table.c.lastname, user_table.c.email, user_table.c.created_at).where(user_table.c.email == email)
        users = conn.execute(statement)
        return users.first()
    
def add_user(firstname, lastname,email, pHash, signup_method, salt, created_at):
    with engine.connect() as conn:
        statement = insert(user_table).values(firstname=firstname, lastname=lastname, email=email, hash=pHash, signup_method=signup_method, salt=salt, created_at=created_at)
        conn.execute(statement)
        conn.commit()