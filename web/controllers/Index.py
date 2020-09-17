from flask import Blueprint
from flask import render_template
index_route = Blueprint('index_page', __name__)


@index_route.route('/')
def index():
    return render_template('index.html')
