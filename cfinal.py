from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:robior123@localhost/microblogging'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class client(db.Model):
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    publisher = db.Column(db.Boolean, nullable=False)
    

    def __init__(self, username, password, publisher):
        self.username = username
        self.password = password
        self.publisher = publisher

class message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(80), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    

    def __init__(self, topic, text):
        self.topic = topic
        self.text = text

if __name__ == '__main__':
    db.create_all()