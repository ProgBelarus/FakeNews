from app import db
from app.catalog.models import Book
from app.auth.models import User


class Evaluation(db.Model):
    __tablename__ = 'evaluation'

    id = db.Column(db.Integer, primary_key=True)
    form_id = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(80), nullable=False)
    comments = db.Column(db.String(1000))
    article_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, form_id, category, comments, article_id, user_id):
        self.form_id = form_id
        self.category = category
        self.comments = comments
        self.article_id = article_id
        self.user_id  = user_id

    @classmethod
    def create_evaluation(cls, form_id, category, comments, article_id, user_id):
        evaluation = cls(form_id, category, comments, article_id, user_id)
        db.session.add(evaluation)
        db.session.commit()
        return evaluation

    def __repr__(self):
        return 'News article titled "{}" is categorized as {} by user {}'.format(
            Book.query.get(self.article_id).title,
            self.category,
            User.query.get(self.user_id).user_email
        )