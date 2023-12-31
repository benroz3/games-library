from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import uuid

app = Flask(__name__)
app.config.from_object(__name__)

# Load environment variables
load_dotenv()

# Enable CORS
CORS(app, resources={r"/*": {'origins': os.environ.get('CLIENT_URL')}})

# dummy data
GAMES = [

    {'id': uuid.uuid4().hex,
        'title': "Assassin's Creed",
        'genre': 'Adventure',
        'played': True,
     },
    {'id': uuid.uuid4().hex,
        'title': 'CSGO',
        'genre': 'Shooter',
        'played': True,
     },
    {'id': uuid.uuid4().hex,
        'title': 'The Last of Us',
        'genre': 'Survival',
        'played': False,
     },
    {'id': uuid.uuid4().hex,
        'title': 'RuneScape',
        'genre': 'MMORPG',
        'played': True,
     },
    {'id': uuid.uuid4().hex,
        'title': 'test',
        'genre': 'test',
        'played': False,
     },
]

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


# The PUT and DELETE route handler
@app.route('/games/<game_id>', methods=['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] = 'Game Updated!'
    if request.method == "DELETE":
        remove_game(game_id)
        response_object['message'] = 'Game removed!'
    return jsonify(response_object)


# Removing the game to update / delete
def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False


if __name__ == "__main__":
    app.run(debug=True)
