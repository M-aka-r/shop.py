from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///shop.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique = True)
    password = db.Column(db.String(512), nullable=False)

    def __repr__(self):
        return f"User: {self.name} | Email: {self.email}"
        

@app.route("/users")
def users():
    users = User.query.all()
    return f"{users}"


@app.route("/create_user")
def create_user():
    user = User(name="Вадим", email="volodimir.popov123@gmail.com", password="12345")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("users"))


with app.app_context():
    db.create_all()

app.run(debug=True)
