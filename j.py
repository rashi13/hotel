from flask import Flask, request, jsonify                                               
from flask_sqlalchemy import SQLAlchemy                                                 
import json                                                                                        
                                                                                        
from . import db
                                                                 
@app.route("/")                                                                         
def hello():                                                                            
      return "Hello, World!"                                                            
                                                                                        
@app.route("/product/<int:id>/", methods=['GET'])                                       
def get_product(id):                                                                    
    if request.method == 'GET':                                                         
        return jsonify(Product.query.get(id).__dict__['title'])
                               
    else:                                                                               
        return 'Product not found'                                                      
@app.route("/products", methods=["POST"])
def add_products():
  if request.method == 'POST':
    ids = request.json['id']
    prices = request.json['price']
    titles = request.json['title']	
    urls = request.json['url']
    descriptions = request.json['description']
    ratings = request.json['rating']

    new_product = Product(id=ids,price=prices,title=titles,url=urls,description=descriptions,rating=ratings)

    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product)

    # return jsonify(Product.query.get(id).__dict__['title'])

@app.route("/productsa/<int:id>", methods=["PUT"])
def prod_update(id):
  if request.method == 'PUT':
    p = Product.query.get(id)
    ttitle = request.json['title']
    uurl = request.json['url']

    p.title = ttitle
    p.url = uurl

    db.session.commit()
    return p_schema.jsonify(p)                                                                                       
class Product(db.Model):                                                                
    id = db.Column(db.Integer, primary_key=True)                                        
    price = db.Column(db.String(10), nullable=False)                                    
    url = db.Column(db.String(10), nullable=False)                                      
    title = db.Column(db.String(80), unique=True, nullable=False)                       
    description = db.Column(db.String(150), unique=True, nullable=False)                       
    rating  = db.Column(db.String(5), nullable=False)                       
                                                                          
    def __repr__(self):                                                               
        return '<Product %r>' % self.title                                              
                                                                                        
if __name__ == "__main__":                                                              
    app.run(debug=True,port=8989)
