from flask import Flask, request, jsonify                                               
from flask_sqlalchemy import SQLAlchemy                                                 
import json                                                                                        
                                                                                        
from . import db
                                                                 
@app.route("/")                                                                         
def hello():                                                                            
      return "Hello, World!"                                                            
                                                                                        
@app.route("/product/<int:trans_id>/", methods=['GET'])                                       
def get_product(trans_id):                                                                    
    if request.method == 'GET':                                                         
        return jsonify(Transaction.query.get(trans_id).__dict__['title'])
                                                                                     
@app.route("/products", methods=["POST"])
def add_trans():
  if request.method == 'POST':
    trans_ids = request.json['trans_id']
    user_ids = request.json['user_id']
    hotel_ids = request.json['hotel_id']	
    totals = request.json['total']
    coupon_discs = request.json['coupon_disc']
    trans_dates = request.json['trans_date']

    new_transaction = Transaction(id=ids,price=prices,title=titles,url=urls,description=descriptions,rating=ratings)

    db.session.add(new_transaction)
    db.session.commit()
    return jsonify(new_product)

    # return jsonify(Product.query.get(id).__dict__['title'])

@app.route("/productsa/<int:trans_id>", methods=["PUT"])
def trans_update(trans_id):
  if request.method == 'PUT':
    p = Product.query.get(id)
    ttitle = request.json['title']
    uurl = request.json['url']

    p.title = ttitle
    p.url = uurl

    db.session.commit()
    return p_schema.jsonify(p)                                                                                       
class Transaction(db.Model):                                                                
    trans_id = db.Column(db.Integer,unique=True, primary_key=True)                                        
    user_id = db.Column(db.Integer, nullable=False)                                    
    hotel_id = db.Column(db.Integer, nullable=False)                                      
    total = db.Column(db.Float)                       
    coupon_disc = db.Column(db.Integer)                       
    trans_date  = db.Column(db.Date, nullable=False)                       
                                                                          
    def __repr__(self):                                                               
        return '<Product %r>' % self.title                                              
                                                                                     
