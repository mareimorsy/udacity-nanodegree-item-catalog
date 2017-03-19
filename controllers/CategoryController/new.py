from . import *
@category.route('/category/new')
def new_category():
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to create a new nanodegree program")
		return redirect('/login')

	return render_template('create_category.html', username = username, picture = picture, user_id = user_id)