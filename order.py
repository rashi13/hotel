from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'order.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Order(db.Model):                                                                
    order_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    item_id = db.Column(db.Integer, nullable=False) 
    quantity = db.Column(db.Integer, nullable=False)                                                            
    price = db.Column(db.Float, nullable=False)     
    user_id = db.Column(db.Integer, nullable=False)  
    hotel_id = db.Column(db.Integer, nullable=False)                                                                                            
    waiter_id = db.Column(db.Integer, nullable=False)                                          

    def __init__(self, order_id, item_id, quantity, price, user_id, hotel_id, waiter_id):
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity
        self.price = price
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.waiter_id = waiter_id


class OrderSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('order_id', 'item_id', 'quantity', 'price', 'user_id', 'hotel_id', 'waiter_id')


order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


# endpoint to create new user
@app.route("/order", methods=["POST"])
def add_order():
    order_id = request.json['order_id']
    item_id = request.json['item_id']
    quantity = request.json['quantity']	
    price = request.json['price']
    user_id = request.json['user_id']
    hotel_id = request.json['hotel_id']
    waiter_id = request.json['waiter_id']

    new_order = Order(order_id, item_id, quantity, price, user_id, hotel_id, waiter_id)

    db.session.add(new_order)
    db.session.commit()
    return jsonify(new_order)



# endpoint to show all users
@app.route("/order", methods=["GET"])
def get_order():
    all_orders = Order.query.all()
    result = orders_schema.dump(all_orders)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/order/<id>", methods=["GET"])
def order_detail(id):
    order = Order.query.get(id)
    return order_schema.jsonify(order)


# endpoint to update user
@app.route("/order/<id>", methods=["PUT"])
def order_update(id):
    order = Order.query.get(id)

    order_id = request.json['order_id']
    item_id = request.json['item_id']
    quantity = request.json['quantity']	
    price = request.json['price']
    user_id = request.json['user_id']
    hotel_id = request.json['hotel_id']
    waiter_id = request.json['waiter_id']


    order.order_id = order_id
    order.item_id = item_id
    order.quantity = quantity
    order.price = price
    order.user_id = user_id
    order.hotel_id = hotel_id
    order.waiter_id = waiter_id
 

    db.session.commit()
    return order_schema.jsonify(order)


# endpoint to delete user
@app.route("/order/<id>", methods=["DELETE"])
def order_delete(id):
    order = Order.query.get(id)
    db.session.delete(order)
    db.session.commit()

    return order_schema.jsonify(order)


if __name__ == '__main__':
    app.run(debug=True)

