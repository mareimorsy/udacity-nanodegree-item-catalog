from . import *
# Update category with new data
@category.route('/category/<int:cat_id>/update', methods=['POST'])
def update_category(cat_id):
	category = session.query(Category).get(int(cat_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to update this nanodegree")
		redirect('/login')
		return # Just in case it didn't redirect for any reason
	# Redirect if not authorized to update
	if category.user.id != user_id:
		flash("You're not allowed to update this nanodegree")
		redirect('/category/%s' % cat_id)
		return # Just in case it didn't redirect for any reason

	category.name = request.form.get('name')
	session.add(category)
	session.commit()
	flash('Nanodegree program has updated successfully!')
	return redirect('/category/%s' % cat_id)