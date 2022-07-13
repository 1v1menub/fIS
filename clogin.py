from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:robior123@localhost/login'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['WTF_CSRF_ENABLED'] = True
app.secret_key = 'secret string'

db = SQLAlchemy(app)

class usuario(db.Model):
    username = db.Column(db.String(80), primary_key=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

if __name__ == '__main__':
    db.create_all()