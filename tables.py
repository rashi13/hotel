from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tables.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Tables(db.Model):
    tables_id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable= False)
    no_of_seats = db.Column(db.Integer)
    reserved =db.Column(db.Boolean)

    def __init__(self,tables_id, hotel_id,no_of_seats,reserved):
        self.hotel_id = hotel_id
        self.tables_id= tables_id
        self.no_of_seats= no_of_seats
        self.reserved= reserved
	


class TablesSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('tables_id','hotel_id','no_of_seats','reserved' )


tables_schema = TablesSchema()
tabless_schema = TablesSchema(many=True)


# endpoint to create new user
@app.route("/tables", methods=["POST"])
def add_tables():
    tables_id = request.json['tables_id']
    hotel_id = request.json['hotel_id']
    no_of_seats= request.json['no_of_seats']
    reserved = request.json['reserved']
    db.session.add(new_tables)
    db.session.commit()

    return jsonify(new_tables)


# endpoint to show all users
@app.route("/tables", methods=["GET"])
def get_tables():
    all_tables = Tables.query.all()
    result = tables_schema.dump(all_tables)
    return jsonify(result.data)


# endpoint to get user detail by id
@app.route("/tables/<id>", methods=["GET"])
def tables_detail(id):
    tables = Tables.query.get(id)
    return tables_schema.jsonify(tables)


# endpoint to update user
@app.route("/tables/<id>", methods=["PUT"])
def tables_update(id):
    tables_id = request.json['tables_id']
    hotel_id = request.json['hotel_id']
    no_of_seats= request.json['no_of_seats']
    reserved = request.json['reserved']

    tables.hotel_id = hotel_id
    tables.no_of_seats = no_of_seats
    tables.reserved = reserved
    tables.tables_id = tables_id
    
    db.session.commit()
    return tables_schema.jsonify(tables)


# endpoint to delete user
@app.route("/tables/<id>", methods=["DELETE"])
def tables_delete(id):
    tables = Tables.query.get(id)
    db.session.delete(tables)
    db.session.commit()

    return user_schema.jsonify(tables)


if __name__ == '__main__':
    app.run(debug=True)

