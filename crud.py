from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    userfirstname = db.Column(db.String(20))
    userlastname = db.Column(db.String(20))
    userphone = db.Column(db.Integer)
    username = db.Column(db.String(20), unique=True)
    userpass = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)

    def __init__(self,userid, userfirstname,userlastname,userphone, username,userpass, email):
        self.userlastname= userlastname
        self.username = username
        self.email = email
        self.userphone= userphone
        self.userpass= userpass
        self.userfirstname= userfirstname
	


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('userid', 'userfirstname','userlastname','userphone','username','userpass' ,'email' )


user_schema = UserSchema()
users_schema = UserSchema(many=True)


# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    userid = request.json['userid']
    userfirstname = request.json['userfirstname']
    userlastname = request.json['userlastname']
    userphone = request.json['userphone']
    userpass = request.json['userpass']
    
    
    
    
    new_user = User(userid,userfirstname,userlastname,userphone,email, username, userpass)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    username = request.json['username']
    email = request.json['email']
    userfirstname = request.json['userfirstname']
    userlastname = request.json['userlastname']
    userphone = request.json['userphone']
    userpass = request.json['userpass']

    user.email = email
    user.username = username
    user.userfirstname = userfirstname
    user.userlastname = userlastname
    user.userphone = userphone
    user.userpass = userpass

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)

