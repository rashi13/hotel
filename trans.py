from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'trans.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Trans(db.Model):                                                                
    trans_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    user_id = db.Column(db.Integer, nullable=False)                                    
    hotel_id = db.Column(db.Integer, nullable=False)                                      
    total = db.Column(db.Float)                       
    coupon_disc = db.Column(db.Integer)                       
    trans_date  = db.Column(db.Date, nullable=False)      

    def __init__(self,trans_id, user_id, hotel_id, total, coupon_disc, trans_date):
        self.trans_id = trans_id
        self.user_id = user_id
        self.hotel_id = hotel_id
        self.total = total
        self.coupon_disc = coupon_disc
        self.trans_date = trans_date


class TransSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('trans_id', 'user_id', 'hotel_id', 'total', 'coupon_disc', 'trans_date')


trans_schema = TransSchema()
transs_schema = TransSchema(many=True)


# endpoint to create new user
@app.route("/products", methods=["POST"])
def add_trans():
    trans_id = request.json['trans_id']
    user_id = request.json['user_id']
    hotel_id = request.json['hotel_id']	
    total = request.json['total']
    coupon_disc = request.json['coupon_disc']
    trans_date = request.json['trans_date']

    new_transaction = Trans(trans_id, user_id, hotel_id, total, coupon_disc, trans_date)

    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(new_transaction)



# endpoint to show all users
@app.route("/trans", methods=["GET"])
def get_trans():
    all_transs = Trans.query.all()
    result = transs_schema.dump(all_transs)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/trans/<id>", methods=["GET"])
def trans_detail(id):
    trans = Trans.query.get(id)
    return trans_schema.jsonify(trans)


# endpoint to update user
@app.route("/trans/<id>", methods=["PUT"])
def trans_update(id):
    trans = Trans.query.get(id)
    trans_ids = request.json['trans_id']
    user_ids = request.json['user_id']
    hotel_ids = request.json['hotel_id']	
    totals = request.json['total']
    coupon_discs = request.json['coupon_disc']
    trans_dates = request.json['trans_date']

    trans.trans_id = trans_id
    trans.user_id = user_id
    trans.hotel_id = hotel_id
    trans.total = total
    trans.coupon_disc = coupon_disc
    trans.trans_date = trans_date
 

    db.session.commit()
    return trans_schema.jsonify(trans)


# endpoint to delete user
@app.route("/trans/<id>", methods=["DELETE"])
def trans_delete(id):
    trans = Trans.query.get(id)
    db.session.delete(trans)
    db.session.commit()

    return trans_schema.jsonify(trans)


if __name__ == '__main__':
    app.run(debug=True)

