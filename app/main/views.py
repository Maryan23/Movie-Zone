from . import main
from flask import render_template


@main.route('/')
def index():
    title = 'Movie Zone'

    return render_template('index.html',title=title)