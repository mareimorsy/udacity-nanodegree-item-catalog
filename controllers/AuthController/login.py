from . import *

@auth.route('/login')
def showLogin():
	# Create anti-forgery state token
	state = ''.join(random.choice(string.ascii_uppercase + string.digits)
	                for x in xrange(32))
	login_session['state'] = state
	return render_template('login.html', STATE=state)