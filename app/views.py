from app import app
from app.models import Hero
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
def getHeroById(hero_id):
    return jsonify(hero = models.Hero.query.get(hero_id).serialize)

@app.route('/api/v1.0/hero/<hero_name>', methods=['GET'])
def getHeroByName(hero_name):
    return jsonify(hero = Hero().query.filter_by(name=hero_name).first().serialize)

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404
