# app/auth/__init__.py
from flask import Blueprint
evaluation = Blueprint('evaluation', __name__, template_folder='templates')
from app.eval import routes