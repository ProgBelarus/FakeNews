# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_heroku import Heroku
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'authentication.do_the_login'
login_manager.session_protection = 'strong'
bcrypt = Bcrypt()
heroku = Heroku()


def create_app(config_type):  # dev, test, or prod

    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    # C:\\Users\\dell\\PycharmProjects\\book_catalog\\config\\dev.py
    app.config.from_pyfile(configuration)
    db.init_app(app)  # initialize database
    bootstrap.init_app(app)  # initialize bootstrap
    login_manager.init_app(app)  # initialize login_manager
    bcrypt.init_app(app)
    heroku.init_app(app)

    from app.admin.views import MyAdminIndexView, AnalyticsView, UserView, EvaluationView, ArticleView
    adm1 = Admin(app, name='Admin Access System', template_mode='bootstrap3', index_view=MyAdminIndexView())

    # Add administrative views here
    from app.auth.models import User
    from app.catalog.models import Book
    from app.catalog.models import Publication
    from app.eval.models import Evaluation
    from app.auth.models import Role

    adm1.add_view(UserView(User, db.session))
    adm1.add_view(ModelView(Role, db.session))
    adm1.add_view(ArticleView(Book, db.session))
    adm1.add_view(ModelView(Publication, db.session))
    adm1.add_view(EvaluationView(Evaluation, db.session))

    adm1.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))

    from app.catalog import main  # import blueprint
    app.register_blueprint(main)  # register blueprint

    from app.eval import eval1
    app.register_blueprint(eval1)

    from app.auth import authentication
    app.register_blueprint(authentication)

    from app.admin import adm
    app.register_blueprint(adm)

    return app