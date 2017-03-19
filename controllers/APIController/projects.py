from . import *

@api.route('/api/projects')
def projects():
	items = session.query(Item).all()
	# items = session.query(Item).order_by("id desc").limit(15).all()
	# #                          .order_by(desc(Item.id))
	return jsonify(Categories = [ i.serialize for i in items])