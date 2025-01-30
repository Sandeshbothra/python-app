from flask import Flask
from apis.users import users
from apis.auth import auth

app = Flask(__name__)
app.register_blueprint(users, url_prefix="/users")
app.register_blueprint(auth, url_prefix="/auth")


@app.route('/')
def hello_world():
   return "Hello World!"


if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8000,debug=True)
