from app import create_app, db
from app.auth.models import User, Role
from app.catalog.webscraper.antiwar_com import add_articles_for_date_to_database
from app.catalog.webscraper.madworldnews_com import add_articles_for_page_to_database
from datetime import datetime
from sqlalchemy import exc

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
        add_articles_for_date_to_database(datetime(2019, 8, 30))
        add_articles_for_page_to_database(1)
    except exc.IntegrityError:
        flask_app.run()


    # if not User.query.filter_by(user_name='administrator').first():
    #     User.create_user(user='administrator', email='admin@admin.com', password='jbaijvnakovninciewvun')
    #     # note: password from harry@potters.com is 'secret'
    # admin_usr = User.query.filter_by(user_name='administrator').first()
    # admin_usr.roles = [Role.query.filter_by(name='Admin').first(), ]
    # db.session.commit()
    # add_articles_for_date_to_database(datetime(2019, 8, 30))
    # add_articles_for_page_to_database(1)
    # flask_app.run()