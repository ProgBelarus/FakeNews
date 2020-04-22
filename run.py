from app import create_app, db
from app.auth.models import User, Role
from sqlalchemy import exc
import app.admin.database_mgmt as db_mgmt

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

    # db_mgmt.clear_database()
    # db_mgmt.load_new_articles(15)
    # if not Role.query.filter_by(name='Admin').first():
    #     Role.create_role(name='Admin')
    # if not User.query.filter_by(user_name='administrator').first():
    #     User.create_user(user='administrator', email='admin@admin.com', password='jbaijvnakovninciewvun')
    #     # note: password from harry@potters.com is 'secret'
    # admin_usr = User.query.filter_by(user_name='administrator').first()
    # admin_usr.roles = [Role.query.filter_by(name='Admin').first(), ]
    # db.session.commit()
    # flask_app.run(use_reloader=False)