from findARestaurant import findARestaurant
from models import Base, Restaurant
from flask import Flask, jsonify, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = 'ZDO41DDL454G0KST35WWI2O0F1XPHC513GA4VM1DHQR2PRKG'
foursquare_client_secret = 'GTZAX2NZGDQOOBZD4PMU4MCTKM4YXHPSYVX5ULWH4H5OZP32'
google_api_key = 'nVtH3TYHHgkwnucDPmdcxMqBNFRFyns'

engine = create_engine('sqlite:///restaruants.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

@app.route('/restaurants', methods = ['GET', 'POST'])
def all_restaurants_handler():

	if request.method == 'GET':
		restaurants = session.query(Restaurant).all()
		return jsonify(restaurants=[i.serialize for i in restaurants])

	elif request.method == 'POST':
		mealType = request.args.get('mealType')
		location = request.args.get('location')

		found = findARestaurant(mealType, location)

		newRestaurant = Restaurant(restaurant_name = unicode(found['name']), restaurant_address = unicode(found['address']), restaurant_image = found['image'])
		session.add(newRestaurant)
		session.commit()
		
		return jsonify(newRestaurant = newRestaurant.serialize)


@app.route('/restaurants/<int:id>', methods = ['GET','PUT', 'DELETE'])
def restaurant_handler(id):
	
	restaurant = session.query(Restaurant).filter_by(id = id).one()
	
	if request.method == 'GET':
		return jsonify(restaurant = restaurant.serialize)

	elif request.method == 'PUT':
		address = request.args.get('address')
		image = request.args.get('image')
		name = request.args.get('name')

		if address:
			restaurant.restaurant_address = address
		if image:
			restaurant.restaurant_image = image
		if name:
			restaurant.restaurant_name = name
		session.commit()
		return jsonify(restaurant = restaurant.serialize)

	elif request.method == 'DELETE':
		session.delete(restaurant)
		session.commit()
		return "Restaurant Deleted"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)