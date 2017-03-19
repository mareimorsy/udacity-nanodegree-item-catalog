from . import *

# Save new category in DB
@category.route('/category/create', methods=['POST'])
def create_category():
	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')
	request.form.get('name')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to create a new nanodegree program")
		return redirect('/login')

	category = Category(name = request.form.get('name'), user_id = user_id)
	session.add(category)
	session.commit()
	flash('Nanodegree program has created successfully!')
	return redirect('/category')