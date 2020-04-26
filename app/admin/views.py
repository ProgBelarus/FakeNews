from flask_admin import Admin, AdminIndexView, BaseView, expose
from flask_security import current_user
from flask_admin.contrib.sqla import ModelView

class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return (current_user.is_authenticated and current_user.user_name == 'administrator')
        # This does the trick rendering the view only if the user is authenticated


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html') #, stri = current_user.user_name)


class UserView(ModelView):
    column_hide_backrefs = False
    column_list = ('user_name', 'user_email', 'registration_date', 'roles', 'evals')

class EvaluationView(ModelView):
    column_hide_backrefs = False
    column_list = ('article_id', 'category', 'comments', 'form_id', 'user_id')

class ArticleView(ModelView):
    column_hide_backrefs = False
    column_list = ('id', 'title', 'subtitle', 'text', 'url', 'pub_date', 'pub_id', 'evals', 'is_gold')