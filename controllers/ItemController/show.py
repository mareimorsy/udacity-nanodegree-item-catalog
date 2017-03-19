from . import *

@item.route('/item/<int:item_id>')
def show_item(item_id):
    item = session.query(Item).get(int(item_id))

    username = login_session.get('username')
    picture = login_session.get('picture')
    user_id = login_session.get('user_id')

    return render_template('item.html', username = username, picture = picture, user_id = user_id, item = item)