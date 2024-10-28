from flask import Flask, request, jsonify
from Engine.HomemadeChessEngine import get_best_move
import chess
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}

@app.get('/programming_languages')
@cross_origin()
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}

@app.route('/testMove', methods=['POST'])
@cross_origin()
def testMove():
    print("TEST MOVE CALLED")
    data = request.get_json()
    board_fen = data.get('board_fen')
    board = chess.Board(board_fen)
    move = get_best_move(board, board.turn)
    return jsonify({'best_move': str(move)})

@app.route('/echo', methods=['POST'])
@cross_origin()
def echo():
    data = request.get_json()  # Get JSON data from the request
    print("HELLO")
    print(data)

    field = data.get('field')  # Extract the 'field' from the JSON data
    return jsonify({'field': field})  # Return the same field in the response
