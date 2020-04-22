from app import db
from datetime import datetime
from sqlalchemy import exc


class Publication(db.Model):
    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False) # url, in our case

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_publication(cls, name):
        publication = cls(name)
        db.session.add(publication)
        db.session.commit()
        return publication

    def __repr__(self):
        return 'Publisher is {}'.format(self.name)


class Article(db.Model):
    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    subtitle = db.Column(db.String(500))
    text = db.Column(db.Text(1000000), nullable=False)
    url = db.Column(db.String(500), index=True)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
    is_gold = db.Column(db.Boolean, default=False)

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
    evals = db.relationship('Evaluation', backref='article', lazy=True)

    def __init__(self, title, subtitle, text, url, pub_date, pub_id, is_gold):

        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.url = url
        self.pub_date = pub_date
        self.pub_id = pub_id
        self.is_gold = is_gold

    @classmethod
    def create_article(cls, title, subtitle, text, url, pub_date, pub_id, is_gold):
        article = cls(title, subtitle, text, url, pub_date, pub_id, is_gold)
        try:
            db.session.add(article)
            db.session.commit()
        except exc.DataError as e:
            print("Article not added. Reason: ", e)
            db.session.rollback()
            return False
        return True

    def __repr__(self):
        return '{} by {}'.format(self.title, Publication.query.get(self.pub_id).name)