from flask import Flask, render_template, request
from longest_word.game import Game
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/")
def home():
    g = Game()
    return render_template("home.html", grid=g.grid)

@app.route("/check", methods=["POST"])
def check():
    logger.info(f"Request grid {request.form['word']}")
    logger.info(f"Request grid {request.form['grid']}")
    g = Game()
    g.grid = list(request.form['grid'])
    is_valid = g.is_valid(request.form['word'])

    logger.info(f"Is valid ? {is_valid}")

    return render_template("check.html", grid=request.form['grid'], word=request.form['word'], is_valid=is_valid)
