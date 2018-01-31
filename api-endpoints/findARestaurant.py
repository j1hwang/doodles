from geocode import getGeocodeLocation
import json
import httplib2

from datetime import date
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "ZDO41DDL454G0KST35WWI2O0F1XPHC513GA4VM1DHQR2PRKG"
foursquare_client_secret = "GTZAX2NZGDQOOBZD4PMU4MCTKM4YXHPSYVX5ULWH4H5OZP32"


def findARestaurant(mealType,location):


	myLocation = getGeocodeLocation(location)
	loc = str(myLocation[0]) + ',' + str(myLocation[1])


	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s&query=%s&v=20180129' % 
		(foursquare_client_id, foursquare_client_secret, loc, mealType) )

	h = httplib2.Http()

	response, content = h.request(url, 'GET')
	result = json.loads(content)

	if result['response']['venues']:
		restaurant = result['response']['venues'][0]
		venue_id = restaurant['id']
		restaurant_name = restaurant['name']

		restaurant_address = restaurant['location']['formattedAddress']
		address = ""
		for i in restaurant_address:
			address += i + " "
		restaurant_address = address

		url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20180129&client_secret=%s' %
			(venue_id, foursquare_client_id, foursquare_client_secret) )
		result = json.loads(h.request(url, 'GET')[1])

		if result['response']['photos']['items']:
			firstpic = result['response']['photos']['items'][0]
			prefix = firstpic['prefix']
			suffix = firstpic['suffix']
			imageURL = prefix + "300x300" + suffix
		else:
			imageURL = "https://cdn.pixabay.com/photo/2016/03/05/19/02/abstract-1238247_960_720.jpg"

		restaurantInfo = {'name':restaurant_name, 'address':restaurant_address, 'image':imageURL}
		# print "Restaurant Name: %s" % restaurantInfo['name']
		# print "Restaurant Address: %s" % restaurantInfo['address']
		# print "Image: %s \n" % restaurantInfo['image']
		return restaurantInfo
	else:
		print "No Restaurants Found for %s" % location
		return "No Restaurants Found"

	
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney Australia")


# https://api.foursquare.com/v2/venues/search?
# client_id=ZDO41DDL454G0KST35WWI2O0F1XPHC513GA4VM1DHQR2PRKG
#&client_secret=GTZAX2NZGDQOOBZD4PMU4MCTKM4YXHPSYVX5ULWH4H5OZP32
#&ll=37.566535,126.9779692&query=Pizza&v=20180130&limit=1&radius=1000

# from findARestaurant import findARestaurant

# result = findARestaurant("Pizza", "Seoul, Korea")
# 4b83a1aaf964a520bd0b31e3
# https://api.foursquare.com/v2/venues/4b83a1aaf964a520bd0b31e3/photos?client_id=ZDO41DDL454G0KST35WWI2O0F1XPHC513GA4VM1DHQR2PRKG&v=20180129&client_secret=GTZAX2NZGDQOOBZD4PMU4MCTKM4YXHPSYVX5ULWH4H5OZP32