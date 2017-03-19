from . import *
# Add new item to a specefic category
# It's okay to let others add item to category they didn't create
@item.route('/category/<int:cat_id>/item/create', methods=['POST'])
def create_item(cat_id):
	category = session.query(Category).get(int(cat_id))

	username = login_session.get('username')
	picture = login_session.get('picture')
	user_id = login_session.get('user_id')

	# Redirect to login if not authenticated
	if not username:
		flash("You must login first, in order to create a new nanodegree program")
		return redirect('/login')

	item = Item(name = request.form.get('name'), description = request.form.get('description'), cat_id = cat_id, user_id = user_id)
	session.add(item)
	session.commit()

	flash("New project has successfully added to %s" % category.name)
	return redirect('/category/%s' % cat_id)


