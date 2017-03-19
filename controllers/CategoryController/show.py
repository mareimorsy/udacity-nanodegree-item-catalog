from . import *

@category.route('/category/<int:cat_id>')
def show_category(cat_id):
	category = session.query(Category).get(int(cat_id))
	# items = category.item
	items =  session.query(Item).filter_by(cat_id=cat_id).all()

	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')
	return render_template('category.html', category = category, items = items, username = username, picture = picture, user_id = user_id)