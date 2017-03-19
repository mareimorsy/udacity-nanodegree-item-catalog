from . import *

@home.route('/')
def showFrontPage():
	username = login_session.get('username')
	picture = login_session.get('picture')
	categories = session.query(Category).all()
	items = session.query(Item).order_by("id desc").limit(15).all()
	#                          .order_by(desc(Item.id))
	return render_template('home.html', categories = categories, items = items, username = username, picture = picture)