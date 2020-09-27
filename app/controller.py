from app import app
from flask import render_template, request
from app.models.rps import *
from app.models.player import *

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/get_result', methods=['POST', 'GET'])
def get_result():
    player_1_name = request.form.get ('player_1_name')
    player_1_choice = request.form.get ('player_1_choice')
    player_1 = Player(player_1_name, player_1_choice)
    player_2_name = request.form.get ('player_2_name')
    player_2_choice = request.form.get ('player_2_choice')
    player_2 = Player(player_2_name, player_2_choice)

    return render_template (index.html, player_1_name, player_1_choice, player_2_name, player_2_choice )