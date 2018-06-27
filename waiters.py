from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'waiters.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Waiter(db.Model):
    waiter_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    waiter_name = db.Column(db.String(20))
    waiter_contact = db.Column(db.Integer)
    waiter_free = db.Column(db.Boolean)
    order_id =db.Column(db.Integer)

    def __init__(self,waiter_id, hotel_id,waiter_name,waiter_contact, waiter_free,order_id):
        self.hotel_id = hotel_id
        self.waiter_name = waiter_name
        self.waiter_contact= waiter_contact
        self.waiter_free= waiter_free
        self.order_id= order_id
        self.userfirstname= userfirstname
	


class WaiterSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'waiter_name','waiter_contact','waiter_free','order_id','waiter_id' )


waiter_schema = WaiterSchema()
waiters_schema = WaiterSchema(many=True)


# endpoint to create new user
@app.route("/waiter", methods=["POST"])
def add_waiter():
    hotel_id = request.json['hotel_id']
    waiter_name = request.json['waiter_name']
    waiter_contact = request.json['waiter_contact']
    waiter_free = request.json['waiter_free']
    order_id = request.json['order_id']
    waiter_id = request.json['waiter_id']
    db.session.add(new_waiter)
    db.session.commit()

    return jsonify(new_waiter)


# endpoint to show all users
@app.route("/waiter", methods=["GET"])
def get_waiter():
    all_waiters = Waiter.query.all()
    result = waiters_schema.dump(all_waiters)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/waiter/<id>", methods=["GET"])
def waiter_detail(id):
    waiter = Waiter.query.get(id)
    return user_schema.jsonify(waiter)


# endpoint to update user
@app.route("/waiter/<id>", methods=["PUT"])
def waiter_update(id):
    hotel_id = request.json['hotel_id']
    waiter_name = request.json['waiter_name']
    waiter_contact = request.json['waiter_contact']
    waiter_free = request.json['waiter_free']
    order_id = request.json['order_id']
    waiter_id = request.json['waiter_id']

    waiter.hotel_id = hotel_id
    waiter.waiter_name = waiter_name
    waiter.waiter_contact = waiter_contact
    waiter.waiter_free = waiter_free
    waiter.order_id = order_id
    waiter.waiter_id= waiter_id
    

    db.session.commit()
    return waiter_schema.jsonify(waiter)


# endpoint to delete user
@app.route("/waiter/<id>", methods=["DELETE"])
def waiter_delete(id):
    waiter = Waiter.query.get(id)
    db.session.delete(waiter)
    db.session.commit()

    return user_schema.jsonify(waiter)


if __name__ == '__main__':
    app.run(debug=True)

