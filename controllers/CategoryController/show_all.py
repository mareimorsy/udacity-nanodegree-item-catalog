from . import *

@category.route('/category')
def show_all_categories():
	categories = session.query(Category).all()

	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')


	return render_template('categories.html', categories = categories, username = username, picture = picture, user_id = user_id)
