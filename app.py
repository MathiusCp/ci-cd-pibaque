# app.py
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import random
import string

app = Flask(__name__)
app.secret_key = "cambia_esta_clave_por_una_segura"  # cámbiala en producción

WORDS = [
    "python", "flask", "programacion", "desarrollo", "computadora",
    "algoritmo", "variable", "funcion", "internet", "despliegue",
    "servidor", "docker", "contener", "repositorio", "git"
]

MAX_ERRORS = 6

def start_new_game():
    word = random.choice(WORDS).lower()
    session["word"] = word
    session["guessed"] = []           # letras adivinadas
    session["errors"] = 0             # errores cometidos
    session["status"] = "playing"     # playing, won, lost

def masked_word():
    word = session.get("word", "")
    guessed = session.get("guessed", [])
    return " ".join([c if c in guessed else "_" for c in word])

def check_game_over():
    word = session.get("word", "")
    guessed = session.get("guessed", [])
    errors = session.get("errors", 0)
    if all(c in guessed for c in word):
        session["status"] = "won"
    elif errors >= MAX_ERRORS:
        session["status"] = "lost"

@app.route("/")
def index():
    # Si no hay juego activo, inicia uno
    if "word" not in session:
        start_new_game()
    return render_template(
        "index.html",
        masked=masked_word(),
        errors=session.get("errors", 0),
        max_errors=MAX_ERRORS,
        guessed=session.get("guessed", []),
        status=session.get("status", "playing"),
        word=session.get("word") if session.get("status") != "playing" else None
    )

@app.route("/new")
def new_game():
    start_new_game()
    return redirect(url_for("index"))

@app.route("/guess", methods=["POST"])
def guess():
    if "word" not in session:
        start_new_game()

    if session.get("status") != "playing":
        return redirect(url_for("index"))

    letter = request.form.get("letter", "").strip().lower()
    if not letter or len(letter) != 1 or letter not in string.ascii_lowercase:
        # invalid input: ignore and redirect
        return redirect(url_for("index"))

    guessed = session.get("guessed", [])
    if letter in guessed:
        return redirect(url_for("index"))  # ya adivinada

    guessed.append(letter)
    session["guessed"] = guessed

    if letter not in session.get("word", ""):
        session["errors"] = session.get("errors", 0) + 1

    check_game_over()
    return redirect(url_for("index"))

# API endpoint opcional (devuelve estado en JSON)
@app.route("/api/state")
def api_state():
    if "word" not in session:
        start_new_game()

    check_game_over()
    return jsonify({
        "masked": masked_word(),
        "errors": session.get("errors", 0),
        "max_errors": MAX_ERRORS,
        "guessed": session.get("guessed", []),
        "status": session.get("status", "playing"),
        "word": session.get("word") if session.get("status") != "playing" else None
    })

if __name__ == "__main__":
    # puerto 8000 para coincidir con otros ejemplos si quieres
    app.run(host="0.0.0.0", port=1011, debug=True)
