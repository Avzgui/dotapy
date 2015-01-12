from app import app
from flask import render_template
from app import db, models

@app.route('/')
@app.route('/index')
def index():
    heroes = models.Hero.query.all()
    return render_template('index.html',
                           title='Home',
                           Heroes=heroes)