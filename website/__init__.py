from flask import Flask


def create_app():
    app = Flask(__name__)
    # Encrypt / secure cookies or session data related to website with String 'key'
    app.config['SECRET_KEY'] = 'key'
    return app
