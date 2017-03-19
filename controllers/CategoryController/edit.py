from . import *

# Show edit form
@category.route('/category/<int:cat_id>/edit')
def editCategory(cat_id):
	category = session.query(Category).get(int(cat_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to update this nanodegree program")
		return redirect('/login')

	# Redirect if not authorized to update
	if category.user.id != user_id:
		flash("You're not allowed to update this nanodegree program")
		return redirect('/category/%s' % cat_id)

	return render_template('edit_category.html', username = username, picture = picture, user_id = user_id, category = category)