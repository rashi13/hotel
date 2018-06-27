from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'cook.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Cook(db.Model):
    cook_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    cook_name = db.Column(db.String(20))
    order_id =db.Column(db.Integer)

    def __init__(self,cook_id, hotel_id,cook_name,order_id):
        self.hotel_id = hotel_id
        self.order_id= order_id
        self.cook_name= cook_name
        self.cook_id= cook_id
	


class CookSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('cook_id','hotel_id','cook_name','order_id' )


cook_schema = CookSchema()
cooks_schema = CookSchema(many=True)


# endpoint to create new user
@app.route("/cook", methods=["POST"])
def add_cook():
    cook_id = request.json['cook_id']
    hotel_id = request.json['hotel_id']
    cook_name = request.json['cook_name']
    order_id = request.json['order_id']
    db.session.add(new_cook)
    db.session.commit()

    return jsonify(new_cook)


# endpoint to show all users
@app.route("/cook", methods=["GET"])
def get_cook():
    all_cook = Cook.query.all()
    result = cook_schema.dump(all_cook)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/cook/<id>", methods=["GET"])
def cook_detail(id):
    cook = Cook.query.get(id)
    return cook_schema.jsonify(cook)


# endpoint to update user
@app.route("/cook/<id>", methods=["PUT"])
def cook_update(id):
    cook_id= request.json['cook_id']
    hotel_id = request.json['hotel_id']
    cook_name = request.json['cook_name']
    order_id = request.json['order_id']

    cook.hotel_id = hotel_id
    cook.cook_name = cook_name
    cook.order_id = order_id
    cook.cook_id = cook_id
    
    db.session.commit()
    return cook_schema.jsonify(cook)


# endpoint to delete user
@app.route("/cook/<id>", methods=["DELETE"])
def cook_delete(id):
    cook = Cook.query.get(id)
    db.session.delete(cook)
    db.session.commit()

    return user_schema.jsonify(cook)


if __name__ == '__main__':
    app.run(debug=True)

