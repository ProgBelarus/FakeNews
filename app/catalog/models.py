from app import db
from datetime import datetime


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


class Book(db.Model):
    __tablename__ = 'book'

    # id = db.Column(db.Integer, primary_key=True)
    # title = db.Column(db.String(500), nullable=False, index=True)
    # author = db.Column(db.String(350))
    # avg_rating = db.Column(db.Float)
    # format = db.Column(db.String(50))
    # image = db.Column(db.String(100), unique=True)
    # num_pages = db.Column(db.Integer)
    # pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    subtitle = db.Column(db.String(500))
    text = db.Column(db.String(50000), nullable=False)
    url = db.Column(db.String(500), index=True)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())

    # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, subtitle, text, url, pub_date, pub_id):
        # self.title = title
        # self.author = author
        # self.avg_rating = avg_rating
        # self.format = book_format
        # self.image = image
        # self.num_pages = num_pages
        # self.pub_id = pub_id

        self.title = title
        self.subtitle = subtitle
        self.text = text
        self.url = url
        self.pub_date = pub_date
        self.pub_id = pub_id

    @classmethod
    def create_article(cls, title, subtitle, text, url, pub_date, pub_id):
        article = cls(title, subtitle, text, url, pub_date, pub_id)
        db.session.add(article)
        db.session.commit()
        return article

    def __repr__(self):
        return '{} by {}'.format(self.title, Publication.query.get(self.pub_id).name)