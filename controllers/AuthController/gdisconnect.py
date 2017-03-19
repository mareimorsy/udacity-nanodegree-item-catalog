from . import *

@auth.route('/gdisconnect')
def gdisconnect():
	# Only disconnect a connected user.
	access_token = login_session.get('access_token')
	if access_token is None:
	    response = make_response(
	        json.dumps('Current user not connected.'), 401)
	    response.headers['Content-Type'] = 'application/json'
	    return response

	url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
	h = httplib2.Http()
	result = h.request(url, 'GET')[0]

	del login_session['access_token']
	del login_session['gplus_id']
	del login_session['username']
	del login_session['email']
	del login_session['picture']
	del login_session['user_id']

	if result['status'] != '200':
	    # For whatever reason, the given token was invalid.
	    response = make_response(
	        json.dumps('Failed to revoke token for given user.'), 400)
	    response.headers['Content-Type'] = 'application/json'
	    return response
	return redirect('/login')