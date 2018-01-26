from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
app = Flask(__name__)

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


## API Endpoint (GET Request) ##
@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuJSON(restaurant_id, menu_id):

	menu = session.query(MenuItem).filter_by(id=menu_id).one()
	return jsonify(MenuItem=[menu.serializeAgain])
#course, desc, id, name ,price
## API Endpoint End ##


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)

    return render_template('menu.html', restaurant=restaurant, items=items)



@app.route('/restaurant/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(
            name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
	if request.method == 'POST':
		
		editMenu = session.query(MenuItem).filter_by(id=menu_id).one()
		if request.form['name']:
			editMenu.name = request.form['name']
		
		session.add(editMenu)
		session.commit() 
		flash("menu item modified!")
		return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))

	else:
		item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
		return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_name=item.name, menu_id=item.id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteMenu = session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(deleteMenu)
        session.commit()
        flash("menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html', item=deleteMenu)




if __name__ == '__main__':
	app.secret_key = 'jL8FMq7a1UTFTs7hLcTb6UjV'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)