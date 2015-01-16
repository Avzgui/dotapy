from app import app
from flask import render_template,jsonify
from app import db, models

@app.route('/')
@app.route('/index')
def index():
    heroes = models.Hero.query.all()
    return render_template('index.html',
                           title='Home',
                           Heroes=heroes)

@app.route('/api/v1.0/hero/<int:hero_id>', methods=['GET'])
def getHero(hero_id):
    return jsonify(hero = models.Hero.query.get(hero_id).serialize)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
