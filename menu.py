from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'menu.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Menu(db.Model):                                                                
    menu_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    name = db.Column(db.String, nullable=False)                                    
    hotel_id = db.Column(db.Integer, nullable=False)                                      
    price = db.Column(db.Float)                       
    available = db.Column(db.Boolean)                       
    discounted  = db.Column(db.String)      
    bestseller  = db.Column(db.String)      

    def __init__(self, menu_id, name, hotel_id, price, available, discounted, bestseller):
        self.menu_id = menu_id
        self.name = name
        self.hotel_id = hotel_id
        self.price = price
        self.available = available
        self.discounted = discounted
        self.bestseller = bestseller


class MenuSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('menu_id', 'name', 'hotel_id', 'price', 'available', 'discounted', 'bestseller')


menu_schema = MenuSchema()
menus_schema = MenuSchema(many=True)


# endpoint to create new user
@app.route("/products", methods=["POST"])
def add_menu():
    menu_id = request.json['menu_id']
    name = request.json['name']
    hotel_id = request.json['hotel_id']	
    price = request.json['price']
    available = request.json['available']
    discounted = request.json['discounted']
    bestseller = request.json['bestseller']

    new_menu = Menu(menu_id, name, hotel_id, price, available, discounted, bestseller)

    db.session.add(new_menu)
    db.session.commit()
    return jsonify(new_menu)



# endpoint to show all users
@app.route("/menu", methods=["GET"])
def get_menu():
    all_menus = Menu.query.all()
    result = menus_schema.dump(all_menus)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/menu/<id>", methods=["GET"])
def menu_detail(id):
    menu = Menu.query.get(id)
    return menu_schema.jsonify(menu)


# endpoint to update user
@app.route("/menu/<id>", methods=["PUT"])
def menu_update(id):
    menu = Menu.query.get(id)

    menu_id = request.json['menu_id']
    name = request.json['name']
    hotel_id = request.json['hotel_id']	
    price = request.json['price']
    available = request.json['available']
    discounted = request.json['discounted']
    bestseller = request.json['bestseller']

    menu.menu_id = menu_id
    menu.name = name
    menu.hotel_id = hotel_id
    menu.price = price
    menu.available = available
    menu.discounted = discounted
    menu.bestseller = bestseller
 

    db.session.commit()
    return menu_schema.jsonify(menu)


# endpoint to delete user
@app.route("/menu/<id>", methods=["DELETE"])
def menu_delete(id):
    menu = Menu.query.get(id)
    db.session.delete(menu)
    db.session.commit()

    return menu_schema.jsonify(menu)


if __name__ == '__main__':
    app.run(debug=True)

