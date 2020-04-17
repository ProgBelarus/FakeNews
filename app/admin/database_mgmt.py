from app.catalog.models import Book, Publication
from app.eval.models import Evaluation
from app.auth.models import User

def clear_database():
    Evaluation.query.delete()
    Book.query.delete()
    Publication.query.delete()
    User.query.delete()