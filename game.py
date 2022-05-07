from flask import Flask, render_template, request, redirect
from sqlite3 import connect
import random

app = Flask(__name__)

words_for_game = []

rooms = [
    {"id": "id", "password": "number"}
]


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/rules')
def rules():
    return render_template("rules.html")


@app.route('/create')
def create_page():
    return render_template("create.html")


@app.route('/create/my_words')
def my_words_page():
    return render_template("my_words.html")

# @app.route('/add_password', methods=['post'])
# def add_password():
#     conn = connect("words.sqlite")
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO rooms (words) VALUES (?)", [""])
#     id = cursor.lastrowid
#     conn.commit()
#     return redirect(f'/my/{id}')


@app.route('/create/my_words', methods=['post'])
def my_words():
    print(request.form)
    for word in request.form.get('words_for_game', "").split("\n"):
        words_for_game.append(word)
    return redirect('/game')

@app.route('/reset')
def reset():
    words_for_game.clear()
    return "reset"

@app.route('/game')
def game():
    return render_template("game.html")


@app.route('/api/word')
def game_word():
    if words_for_game:
        result = random.choice(words_for_game)
        return result
    else:
        return "no words"


@app.route('/api/delete', methods=['post'])
def delete_word():
    word = request.form.get('word', '')
    if word in words_for_game:
        words_for_game.remove(word)
    return str(len(words_for_game))


# @app.route('/join')
# def join_page():
#     return render_template('join.html')
#
# # @app.route('/join', methods='post')
# # def join():
# #     id = request.form.get("id")
# #     return redirect(f'/game/{ id }')

app.run(debug=False, host="0.0.0.0", port=8081)
