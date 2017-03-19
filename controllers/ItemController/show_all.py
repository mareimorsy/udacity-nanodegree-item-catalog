from . import *

@item.route('/item')
def show_all_items():
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')
	items = session.query(Item).order_by("id desc").limit(100).all()
	return render_template('items.html', items = items, username = username, picture = picture, user_id = user_id)
