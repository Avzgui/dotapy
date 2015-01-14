__author__ = 'antoine'

from app import db

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(120))
    mainStats = db.Column(db.String(120))
    baseAgility = db.Column(db.Float(4))
    baseStrength = db.Column(db.Float(4))
    baseIntelligence = db.Column(db.Float(120))
    gainAgility = db.Column(db.Float(120))
    gainStrength = db.Column(db.Float(120))
    gainIntelligence = db.Column(db.Float(120))
    affiliation = db.Column(db.String(50))
    damageMin = db.Column(db.Integer)
    damageMax = db.Column(db.Integer)
    armor = db.Column(db.Float(4))
    moveSpeed = db.Column(db.Float(4))
    baseAttackTime = db.Column(db.Float(4))
    castingAnimationPoint = db.Column(db.Float(4))
    castingAnimationBackswing = db.Column(db.Float(4))
    attackAnimationPoint = db.Column(db.Float(4))
    attackAnimationBackswing = db.Column(db.Float(4))
    attackRangeValue = db.Column(db.Float(4))
    attackRangeType = db.Column(db.Float(4))
    missileSpeed = db.Column(db.Float(4))
    introduction = db.Column(db.String(120))
    background = db.Column(db.String(120))
    sightRangeDay = db.Column(db.Float(4))
    sightRangeNight = db.Column(db.Float(4))

    def __repr__(self):
        return '<Hero %r>' % (self.name + ' - ' + self.surname)
