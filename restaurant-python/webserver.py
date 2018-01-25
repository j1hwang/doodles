from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

class webserverHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith("/restaurants"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				restaurants = session.query(Restaurant).all()

				output = ""
				output = "<html><body>"

				for restaurant in restaurants:
					output += restaurant.name + " (" + str(restaurant.id) + ")<br>\
						<a href='/restaurants/" + str(restaurant.id) + "/edit'>edit</a><br>\
						<a href='/restaurants/" + str(restaurant.id) + "/delete'>delete</a><br><br>"

				output += "<br><a href='/restaurants/new'>create new restaurant</a>"
				output += "</body></html>"
				
				self.wfile.write(output)
				return


			if self.path.endswith("/restaurants/new"):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()

				output = ""
				output = "<html><body>\
					<form method='POST' enctype='multipart/form-data'\
					action='/restaurants/new'>\
					<h2>make a new restaurant</h2>\
					<input name='restaurante' type='text'>\
					<input type='submit' value='create'>\
					</form></body></html>"

				self.wfile.write(output)
				return


			if self.path.endswith("/edit"):
				
				resId = self.path.split('/')[2]
				restaurant = session.query(Restaurant).filter_by(id=resId).one()

				if restaurant:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()

					output = ""
					output = "<html><body>\
						<form method='POST' enctype='multipart/form-data'\
						action='/restaurants/" + resId + "/edit'>\
						<h2>" + restaurant.name + " ("+ resId + ")</h2>\
						<input name='newName' type='text'>\
						<input type='submit' value='edit'>\
						</form></body></html>"

					self.wfile.write(output)


			if self.path.endswith("/delete"):
				
				resId = self.path.split('/')[2]
				restaurant = session.query(Restaurant).filter_by(id=resId).one()

				if restaurant:
					self.send_response(200)
					self.send_header('Content-type', 'text/html')
					self.end_headers()

					output = ""
					output = "<html><body>\
						<form method='POST' enctype='multipart/form-data'\
						action='/restaurants/" + resId + "/delete'>\
						<h2>are you sure to delete " + restaurant.name + " ("+ resId + ")?</h2>\
						<input type='submit' value='delete'>\
						</form></body></html>"

					self.wfile.write(output)


		except IOError:
			self.send_error(404, "File Not Found %s" % self.path) 



	def do_POST(self):
		try:
			if self.path.endswith("/restaurants/new"):
				
				ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					messagecontent = fields.get('restaurante')

					print 'added : ' + messagecontent[0]
					
					addRestaurant = Restaurant(name = messagecontent[0])
					session.add(addRestaurant)
					session.commit()

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants')
					self.end_headers()


			if self.path.endswith("/edit"):
				
				ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)
					newName = fields.get('newName')
					resId = self.path.split('/')[2]

					editRestaurant = session.query(Restaurant).filter_by(id=resId).one()
					editRestaurant.name = newName[0]
					session.add(editRestaurant)
					session.commit() 

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants')
					self.end_headers()


			if self.path.endswith("/delete"):
				
				ctype, pdict = cgi.parse_header(self.headers.getheader('Content-type'))
				if ctype == 'multipart/form-data':
					fields = cgi.parse_multipart(self.rfile, pdict)

					resId = self.path.split('/')[2]

					deleteRestaurant = session.query(Restaurant).filter_by(id=resId).one()
					session.delete(deleteRestaurant)
					session.commit() 

					self.send_response(301)
					self.send_header('Content-type', 'text/html')
					self.send_header('Location', '/restaurants')
					self.end_headers()		
 
		except:
			pass

def main():
	try:
		port = 8080
		server = HTTPServer( ('', port), webserverHandler ) #request handler
		print "Web server running on port %s" % port
		server.serve_forever()

	except KeyboardInterrupt:
		print "^C entered, stopping web server..."
		server.socket.close()


if __name__ == '__main__':
	main()