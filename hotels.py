from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'hotels.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Hotels(db.Model):
    hotel_id = db.Column(db.Integer, primary_key=True)
    hotel_name = db.Column(db.String(20))
    hotel_address = db.Column(db.String(80))
    hotel_phone = db.Column(db.Integer)
    hotel_email = db.Column(db.String(50), unique=True)
    hotel_lat = db.Column(db.Float)
    hotel_long = db.Column(db.Float)
    hotel_capacity = db.Column(db.Integer)
    hotel_open = db.Column(db.Time)
    hotel_close = db.Column(db.Time)
    hotel_desc = db.Column(db.String(200))
    hotel_stars = db.Column(db.Float)
    hotel_menupic = db.Column(db.String(2000))
    hotel_hotelpic = db.Column(db.String(2000))
    hotel_avgcost = db.Column(db.Float)
    hotel_moreinfo = db.Column(db.String(2000))

    def __init__(self,hotel_id, hotel_name,hotel_address,hotel_open,hotel_close,hotel_desc,hotel_stars,hotel_menupic,      hotel_hotelpic,hotel_avgcost,hotel_moreinfo,hotel_phone, hotel_email,hotel_lat, hotel_long,hotel_capacity):
        self.hotel_id= hotel_id
        self.hotel_name = hotel_name
        self.hotel_address  = hotel_address
        self.hotel_open= hotel_open
        self.hotel_close= hotel_close
        self.hotel_desc= hotel_desc
        self.hotel_stars= hotel_stars
        self.hotel_menupic= hotel_menupic
        self.hotel_hotelpic = hotel_hotelpic
        self.hotel_avgcost  = hotel_avgcost
        self.hotel_moreinfo= hotel_moreinfo
        self.hotel_phone= hotel_phone
        self.hotel_email= hotel_email
        self.hotel_lat= hotel_lat
        self.hotel_long= hotel_long
        self.hotel_capacity= hotel_capacity
        


class HotelsSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('hotel_id', 'hotel_name','hotel_address','hotel_open','hotel_moreinfo','hotel_phone', 'hotel_email','hotel_lat', 'hotel_long','hotel_capacity', 'hotel_desc','hotel_stars','hotel_menupic','hotel_close','hotel_hotelpic','hotel_avgcost')


hotels_schema = HotelsSchema()
hotelss_schema = HotelsSchema(many=True)


# endpoint to create new hotels
@app.route("/hotels", methods=["POST"])
def add_hotels():
    hotel_id = request.json['hotel_id']
    hotel_name = request.json['hotel_name']
    hotel_address = request.json['hotel_address']
    hotel_open = request.json['hotel_open']
    hotel_moreinfo = request.json['hotel_moreinfo']
    hotel_phone = request.json['hotel_phone']
    hotel_email = request.json['hotel_email']
    hotel_lat = request.json['hotel_lat']
    hotel_long = request.json['hotel_long']
    hotel_capacity = request.json['hotel_capacity']
    hotel_desc = request.json['hotel_desc']
    hotel_stars = request.json['hotel_stars']
    hotel_menupic = request.json['hotel_menupic']
    hotel_close = request.json['hotel_close']
    hotel_hotelpic = request.json['hotel_hotelpic']
    hotel_avgcost = request.json['hotel_avgcost']
    
    
    
    
    new_hotels = Hotels(hotel_id, hotel_name,hotel_address,hotel_open,hotel_close,hotel_desc,hotel_stars,hotel_menupic,      hotel_hotelpic,hotel_avgcost,hotel_moreinfo,hotel_phone, hotel_email,hotel_lat, hotel_long,hotel_capacity)

    db.session.add(new_hotels)
    db.session.commit()

    return jsonify(new_hotels)


# endpoint to show all hotelss
@app.route("/hotels", methods=["GET"])
def get_hotels():
    all_hotelss = Hotels.query.all()
    result = hotelss_schema.dump(all_hotelss)
    return jsonify(result.data)


# endpoint to get hotels detail by id
@app.route("/hotels/<id>", methods=["GET"])
def hotels_detail(id):
    hotels = Hotels.query.get(id)
    return hotels_schema.jsonify(hotels)


# endpoint to update hotels
@app.route("/hotels/<id>", methods=["PUT"])
def hotels_update(id):
    hotelsname = request.json['hotelsname']
    email = request.json['email']
    hotelsfirstname = request.json['hotelsfirstname']
    hotelslastname = request.json['hotelslastname']
    hotelsphone = request.json['hotelsphone']
    hotelspass = request.json['hotelspass']

    hotels.hotel_id= hotel_id
    hotels.hotel_name = hotel_name
    hotels.hotel_address  = hotel_address
    hotels.hotel_open= hotel_open
    hotels.hotel_close= hotel_close
    hotels.hotel_desc= hotel_desc
    hotels.hotel_stars= hotel_stars
    hotels.hotel_menupic= hotel_menupic
    hotels.hotel_hotelpic = hotel_hotelpic
    hotels.hotel_avgcost  = hotel_avgcost
    hotels.hotel_moreinfo= hotel_moreinfo
    hotels.hotel_phone= hotel_phone
    hotels.hotel_email= hotel_email
    hotels.hotel_lat= hotel_lat
    hotels.hotel_long= hotel_long
    hotels.hotel_capacity= hotel_capacity

    db.session.commit()
    return hotels_schema.jsonify(hotels)


# endpoint to delete hotels
@app.route("/hotels/<id>", methods=["DELETE"])
def hotels_delete(id):
    hotels = Hotels.query.get(id)
    db.session.delete(hotels)
    db.session.commit()

    return hotels_schema.jsonify(hotels)


if __name__ == '__main__':
    app.run(debug=True)

