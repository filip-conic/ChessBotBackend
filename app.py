from flask import Flask, request, jsonify
from Engine.HomemadeChessEngine import get_best_move
import chess
from flask_cors import CORS, cross_origin
from HomemadeEngine.ChessEngine import negamax_get_best_move

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/testMove', methods=['POST'])
@cross_origin()
def testMove():
    print("TEST MOVE CALLED")
    data = request.get_json()
    board_fen = data.get('board_fen')
    board = chess.Board(board_fen)
    best_move = negamax_get_best_move(board, 3)
    print("Best Move: " + str(best_move))
    return jsonify({'best_move': str(best_move)})

@app.route('/testGet', methods=['GET'])
@cross_origin()
def testGet():
    print("TEST GET CALLED")
    # data = request.get_json()
    # board_fen = data.get('board_fen')
    # board = chess.Board(board_fen)
    # best_move = negamax_get_best_move(board, 3)
    best_move = "TEST GET CALLED"
    print("Best Move: " + str(best_move))
    return jsonify({'best_move': str(best_move)})

@app.route('/calculateBestMove', methods=['POST'])
@cross_origin()
def calculateBestMove():
    print("Calculate Best Move Called")
    data = request.get_json()
    board_fen = data.get('board_fen')
    board = chess.Board(board_fen)
    best_move = negamax_get_best_move(board, 3, use_quiet_search=False)
    print("Best Move: " + str(best_move) + "\n")
    return jsonify({'best_move': str(best_move)})

@app.route('/echo', methods=['POST'])
@cross_origin()
def echo():
    data = request.get_json()  # Get JSON data from the request
    print("HELLO")
    print(data)

    field = data.get('field')  # Extract the 'field' from the JSON data
    return jsonify({'field': field})  # Return the same field in the response
