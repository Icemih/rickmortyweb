from flask import Flask
from index import index_blueprint
from flask_sqlalchemy import SQLAlchemy

def main():
    application = Flask(__name__)

    application.config.from_object("config.DevelopementConfig")

    application.register_blueprint(index_blueprint)

    application.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()