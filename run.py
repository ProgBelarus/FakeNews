from app import create_app, db
from app.auth.models import User, Role
from sqlalchemy import exc
from app.admin.database_mgmt import clear_database
from app.catalog.load_articles import load_new_articles_to_database

flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()

    try:
        if not User.query.filter_by(user_name='administrator').first():
            User.create_user(user='administrator', email='admin@admin.com', password='jbaijvnakovninciewvun')
            # note: password from harry@potters.com is 'secret'
        admin_usr = User.query.filter_by(user_name='administrator').first()
        admin_usr.roles = [Role.query.filter_by(name='Admin').first(), ]
        db.session.commit()
    except exc.IntegrityError:
        flask_app.run()

    # clear_database()
    # load_new_articles_to_database(15)
    # if not User.query.filter_by(user_name='administrator').first():
    #     User.create_user(user='administrator', email='admin@admin.com', password='jbaijvnakovninciewvun')
    #     # note: password from harry@potters.com is 'secret'
    # admin_usr = User.query.filter_by(user_name='administrator').first()
    # admin_usr.roles = [Role.query.filter_by(name='Admin').first(), ]
    # db.session.commit()
    # flask_app.run()