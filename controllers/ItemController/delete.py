from . import *
# Show edit form
@item.route('/category/<int:cat_id>/item/<int:item_id>/delete', methods=['POST'])
def delete_Item(cat_id, item_id):
	item = session.query(Item).get(int(item_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to create a new nanodegree program")
		return redirect('/login')

	# Redirect if not authorized to update
	if item.user.id != user_id:
		flash("You're not allowed to delete this nanodegree")
		return redirect('/category/%s' % cat_id)

	session.delete(item)
	session.commit()

	flash("The project has successfully deleted")
	return redirect('/category/%s' % cat_id)