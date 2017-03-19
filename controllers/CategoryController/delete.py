from . import *
# Show edit form
@category.route('/category/<int:cat_id>/delete', methods=['POST'])
def delete_category(cat_id):
	category = session.query(Category).get(int(cat_id))
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to delete this nanodegree")
		return redirect('/login')

	# Redirect if not authorized to update
	if category.user.id != user_id:
		flash("You're not allowed to delete this nanodegree")
		return redirect('/category/%s' % cat_id)

	category.name = request.form.get('name')

	# items =  session.query(Item).filter_by(cat_id=cat_id).all()
	session.delete(category)
	session.commit()
	flash('Nanodegree program has deleted successfully!')
	return redirect('/category')