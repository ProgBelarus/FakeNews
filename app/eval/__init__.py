# app/auth/__init__.py
from flask import Blueprint
eval1 = Blueprint('eval1', __name__, template_folder='templates')
from app.eval import routes