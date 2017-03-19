from . import *
# Update item with new data
@item.route('/category/<int:cat_id>/item/<int:item_id>/update', methods=['POST'])
def update_category(cat_id, item_id):
	item = session.query(Item).get(int(item_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to update this project")
		return redirect('/login')

	# Redirect if not authorized to update
	if item.user.id != user_id:
		flash("You're not allowed to update this project")
		return redirect('/category/%s' % cat_id)

	item.name = request.form.get('name')
	item.description = request.form.get('description')
	session.add(item)
	session.commit()
	flash("The project has updated successfully!")

	return redirect('/category/%s'% cat_id)