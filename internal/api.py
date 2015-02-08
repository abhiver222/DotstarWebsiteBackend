from flask import request, session, Response
from flask.blueprints import Blueprint


api = Blueprint('/api', __name__)


@api.before_request
def auth():
    if not session.get('netid'):
        return Response(status='403')


@api.route('/users')
def search_users():
    '''
    search for users
    '''
    pass


@api.route('/users/<netid>', methods=['GET', 'PUT'])
def manage_user(netid): 
    '''
    get details of a user or update it
    '''
    pass


@api.route('/teams', methods=['GET', 'POST'])
def manage_teams(): 
    '''
    search for teams or create a new team
    '''
    pass


@api.route('/teams/<teamid>', methods=['GET', 'PUT'])
def manage_team(teamid): 
    '''
    get or update a team
    '''
    pass


@api.route('/companies', methods=['GET', 'POST'])
def manage_companies(): 
    '''
    search for companies or create a new company
    '''
    pass


@api.route('/companies/<company_id>', methods=['GET', 'PUT'])
def manage_company(company_id): 
    '''
    get or update a company
    '''
    pass

@api.route('/tasks', methods=['GET', 'POST'])
def manage_tasks(): 
    '''
    search for tasks or create a new task
    '''
    pass


@api.route('/tasks/<task_id>', methods=['GET', 'PUT'])
def manage_task(task_id): 
    '''
    get or update a task
    '''
    pass
