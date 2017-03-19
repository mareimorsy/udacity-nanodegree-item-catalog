from . import *

@item.route('/category/<int:cat_id>/item/new')
def new_item(cat_id):
    category = session.query(Category).get(int(cat_id))

    username = login_session.get('username')
    picture = login_session.get('picture')
    user_id = login_session.get('user_id')

    # Redirect to login if not authenticated
    if not username:
    	flash("You must login first, in order to add new project.")
    	return redirect('/login')

    return render_template('create_item.html', username = username, picture = picture, category = category)