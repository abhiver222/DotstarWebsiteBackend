'''
UI stuff for the server, namely login and registration
'''
from flask import render_template, request, g, session, Blueprint, redirect
import random, urllib, db, cStringIO
from functools import wraps
from urllib import urlencode
from forms import basic_info
from PIL import Image

ui = Blueprint('/', __name__)


PROFILE_MESSAGE = "Hi there! Could you tell us a little about yourself?"
COURSE_NAME = "(dot)*"

def generate_page(name,css,js,description):
    return {
        "course_name" : COURSE_NAME,
        "title" : "CS 196, {0}".format(COURSE_NAME),
        "name" : name,
        "description" : description,
        "home" : "localhost:5000",
        "custom_css" : "{0}.css".format(css),
        "custom_js" : "{0}.js".format(js)
    }


def require_login(view):

    @wraps(view)
    def protected_view(*args, **kwargs):
        if loggedin():
            return view(*args, **kwargs)
        else:
            redirect_args = urlencode({'redirect': request.url})
            return redirect('/login?%s'% redirect_args)

    return protected_view


def loggedin():
    return session.get('netid') is not None


@ui.route('/login', methods=['GET', 'POST'])
def login():
    if loggedin():
        return redirect('/')
        
    unique = {
        "login_saying" : "Welcome to {0}".format(COURSE_NAME),
        "login_details" : "<a href='go'>Fill out a <i>new</i> form</a> if you cannot log in and <u>are officially registered</u>",
        "extra_class" : ''
    }

    page = generate_page("Login",
                        "login",
                        "login",
                        "Welcome to CS 196, {0}. You've never before taken a course like this.".format(COURSE_NAME))

    if request.method == 'GET':
        redirect_url = request.args.get('redirect', '/')
        return render_template('login.html',**locals())
    else:
        netid = request.form['username']
        uin = request.form['password']
        if not db.verify_user(netid, uin):
            funnies = ['Nuts', 'Good grief', 'Goodness gracious', 'Holy guacamole', 'Aww snap', 'Wholly smokes', 'Dagnabbit']
            second_funny = ['that didn\'t work', 'try again', 'that\'s wrong']
            unique['login_details'] = "{0}; {1}! Please fill <a href='go'>this</a> out if you can't log in and <b>are officially registered</b>".format(random.choice(funnies),random.choice(second_funny))
            unique['extra_class'] = 'warning'
            return render_template('login.html', **locals())
        session['netid'] = netid
        redirect_url = request.form['redirect']
        return redirect(redirect_url)


@ui.route('/logout')
def logout():
    session.pop('netid', None)
    return redirect('/login')


@ui.route('/profile', methods=['POST','GET'])
@require_login
def profile():
    if request.method=='GET':
        page = generate_page("Welcome to {0}".format(COURSE_NAME), "index", "", "Welcome to CS 196, {0}. You've never before taken a course like this.".format(COURSE_NAME))
        unique = db.get_user_details(session['netid'])
        questions = basic_info.get_questions(unique)
        return render_template('profile.html',page=page,unique=unique,questions=questions,message=PROFILE_MESSAGE)
    else:
        github = request.form['Github']
        euler = request.form['Euler']
        check_github = urllib.urlopen('https://github.com/{0}'.format(github))
        check_euler = True
        try:
            Image.open(cStringIO.StringIO(urllib.urlopen('https://projecteuler.net/profile/{0}.png'.format(euler)).read()))
        except IOError:
            check_euler = False
            
        if check_euler and check_github.getcode()==200:
            year = request.form['Year']
            email = request.form['Email']
            phone = request.form['Phone']
            skills = request.form['Skills']
            wants = request.form['Wants']
            db.update_user_details(year,
                                   email,
                                   github,
                                   euler,
                                   phone,
                                   skills,
                                   wants,
                                   session['netid'])
            message = "Thanks a lot! We updated your information."
        elif not check_euler:
            message = "We couldn't find your Project Euler account! If you're sure the account exists, email gdyer2@illinois.edu"
        else:
            message = "We couldn't find your GitHub account! If you're sure the account exists, email gdyer2@illinois.edu"
        page = generate_page("Welcome to {0}".format(COURSE_NAME), "index", "", "Welcome to CS 196, {0}. You've never before taken a course like this.".format(COURSE_NAME))
        unique = db.get_user_details(session['netid'])
        questions = basic_info.get_questions(unique)
        return render_template('profile.html', **locals())


@ui.route('/go')
def go_to_form():
    return redirect('http://goo.gl/forms/FSdCBIydoK')

@ui.route('/', methods=['POST', 'GET'])
@require_login
def index():
    return redirect('/profile')
