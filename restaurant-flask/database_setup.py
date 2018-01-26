# configuration UDACITY 1-15

import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


#class definition
class Restaurant(Base):

	#table information
	__tablename__ = 'restuarant'

	# mapper
	name = Column( String(80), nullable = False )
	id = Column( Integer, primary_key = True )

class MenuItem(Base):

	#table information
	__tablename__ = 'menu_item'

	# mapper
	name = Column( String(80), nullable = False )
	id = Column( Integer, primary_key = True )
	course = Column( String(250) )
	description = Column( String(250) )
	price = Column( String(8) )

	restaurant_id = Column( Integer, ForeignKey('restuarant.id') )
	restaurant = relationship(Restaurant)

	@property
	def serialize(self):

	    return {
	        'name': self.name,
	        'description': self.description,
	        'id': self.id,
	        'price': self.price,
	        'course': self.course,
	    }

#course, desc, id, name ,price
	@property
	def serializeAgain(self):

	    return {
	    	'course': self.course,
	    	'description': self.description,
	        'id': self.id,
	        'name': self.name,
	        'price': self.price,	        
	    }

## insert at the end of file - configuration ##
engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.create_all(engine)