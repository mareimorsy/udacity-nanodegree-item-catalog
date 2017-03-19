from . import *

@api.route('/api/programs')
def programs():
	categories = session.query(Category).all()
	return jsonify(Categories = [ i.serialize for i in categories])