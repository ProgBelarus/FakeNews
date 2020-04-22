from app.catalog.models import Article, Publication
from app.eval.models import Evaluation
from app.auth.models import User
from app.webscraper import load_new_articles_to_database

def clear_database():
    Evaluation.query.delete()
    Article.query.delete()
    Publication.query.delete()
    User.query.delete()

def load_new_articles(num_load):
    load_new_articles_to_database(num_load)