from flask import Flask
from controllers import *

app = Flask(__name__)

# +--------+--------------------------------------------+-------------------------------+
# | Method | URI                  	   				    | Action				    	|				|
# +--------+--------------------------------------------+-------------------------------+
# | GET    | /											| HomeController@home			|
# |  	   |											|								|
# | GET    | /category 									| CategoryController@show_all	|
# | GET    | /category/<cat_id> 						| CategoryController@show   	|
# | GET    | /category/<cat_id>/edit 					| CategoryController@edit   	|
# | POST   | /category/<cat_id>/update 					| CategoryController@update   	|
# | GET    | /category/new   							| CategoryController@new    	|
# | POST   | /category/create 							| CategoryController@create   	|
# | POST   | /category/<cat_id>/delete 					| CategoryController@delete   	|
# |  	   |											|								|
# | GET    | /item  									| ItemController@show_all		|
# | GET    | /item/<item_id> 	 						| ItemController@show   		|
# | GET    | /category/<cat_id>/item/<item_id>/edit 	| ItemController@edit   		|
# | POST   | /category/<cat_id>/item/<item_id>/update 	| ItemController@update   		|
# | GET    | /category/<cat_id>/item/new   			    | ItemController@new    		|
# | POST   | /category/<cat_id>/item/create 			| ItemController@create   		|
# | POST   | /category/<cat_id>/item/<item_id>/delete 	| ItemController@delete   		|
# +--------+--------------------------------------------+-------------------------------+

if __name__ == "__main__":
    app.register_blueprint(home)
    app.register_blueprint(category)
    app.register_blueprint(item)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.secret_key = 'Here !s a t0ttaly random $ecret key c@n you gue$$ it?'
    app.run(host='0.0.0.0', port=80, debug=True)