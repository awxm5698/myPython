from flask import render_template
from flask import Flask

from flask import Blueprint
login = Blueprint('login', __name__)


@login.route('/')
def hello_world():
    return render_template('home.html')