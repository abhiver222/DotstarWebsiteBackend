from flask import Flask, current_app
from ui import ui
from api import api
import config,sys

def load_db_conf():
    current_app.db_config = {}
    current_app.db_config['host'] = config.DB_HOST
    current_app.db_config['port'] = config.DB_PORT
    current_app.db_config['user'] = config.DB_USER
    current_app.db_config['db'] = config.DB_NAME
    current_app.db_config['passwd'] = config.DB_PASSWORD


def create_app():
    app = Flask(__name__)
    app.register_blueprint(ui, url_prefix='')
    app.register_blueprint(api, url_prefix='/api')
    with app.app_context():
        load_db_conf()
    return app

# duplicates for python-anywhere limitations
app = create_app()
app.secret_key = config.SECRET_KEY


def setup_db(app):
    '''
    for debug only,
    change it to a real database later
    '''
    import pymysql as sql
    import os
    import db
    basedir = os.path.dirname(os.path.abspath(__file__))
    schema_fname = os.path.normpath(os.path.join(basedir, '..', 'sql', 'sql.sql'))
    with app.app_context():
        cur = db.get_cursor()

        with open(schema_fname) as schema:
            statements = schema.read()
            for stmt in statements.split(';'):
                print stmt
                try:
                    cur.execute(stmt)
                except Exception as e:
                    print 'SQL exec error:', e, 'proceeding...'


if __name__ == '__main__':
    app = create_app()
    app.secret_key = config.SECRET_KEY
    if len(sys.argv) == 2 and sys.argv[1] == 'syncdb':
        setup_db(app)
    else:
        app.run(debug=True)
