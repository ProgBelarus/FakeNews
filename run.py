from app import create_app, db
from app.auth.models import User
from app.catalog.webscraper.antiwar_com import add_articles_for_date_to_database
from datetime import datetime

flask_app = create_app('dev')
with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry', email='harry@potters.com', password='secret')
    add_articles_for_date_to_database(datetime(2019, 8, 30))
flask_app.run()