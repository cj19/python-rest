from flask import Blueprint

routes = Blueprint('routes', __name__)

from .hello import hello
from .user import get_all
