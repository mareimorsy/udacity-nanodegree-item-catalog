from . import *

# Show edit form
@item.route('/category/<int:cat_id>/item/<int:item_id>/edit')
def editItem(cat_id, item_id):
	category = session.query(Category).get(int(cat_id))
	item = session.query(Item).get(int(item_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to edit this project")
		return redirect('/login')

	# Redirect if not authorized to update
	if item.user.id != user_id:
		flash("You're not allowed to edit this project")
		return redirect('/category/%s' % cat_id)

	return render_template('edit_item.html', item = item, username = username, user_id = user_id, picture = picture)