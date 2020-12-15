from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Production, Development

app = Flask(__name__)

app.config.from_object(Development)
# app.config.from_object(Production)

# instance of sqlalchemy
db = SQLAlchemy(app)

from models.Admin import AdminModel

# create tables
@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return 'diani'


if __name__ == '__main__':
    app.run()
