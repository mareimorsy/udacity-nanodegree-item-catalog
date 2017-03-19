from . import *

@api.route('/api/aio')
def all_in_on():

	categories = session.query(Item).all()

	categories_arr = []
	for category in categories:
		items =  session.query(Item).filter_by(cat_id=category.id).all()
		items_arr = []
		for item in items:
			items_arr.append(item.serialize)
		category_items = category.serialize
		category_items['items'] = items_arr
		categories_arr.append(category_items)
	return jsonify(Categories = categories_arr)