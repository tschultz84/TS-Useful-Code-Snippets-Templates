# app.py
from flask import Flask

app = Flask(__name__, static_folder="static")

def create_app():

    _app = Flask(__name__, static_folder="static")

    # This creates a blueprint of all functions in main.py. 
    from main import main as main_blueprint
    _app.register_blueprint(main_blueprint)

    return _app

app = create_app()

if __name__ == '__main__':
    app.run()