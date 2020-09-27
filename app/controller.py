from app import app
from flask import render_template
from app.models.game_format import *
from app.models.game import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')