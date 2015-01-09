__author__ = 'antoine'

from app import db

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    surname = db.Column(db.String(120))
    MainStats = db.Column(db.String(120))
    baseAgility = db.Column(db.Float(4))
    baseStrength = db.Column(db.Float(4))
    baseIntelligence = db.Column(db.Float(120))
    gainAgility = db.Column(db.Float(120))
    gainStrength = db.Column(db.Float(120))
    gainIntelligence = db.Column(db.Float(120))
    affiliation = db.Column(db.String(50))
    damageMin = db.Column(db.Integer(4))
    damageMax = db.Column(db.Integer(4))
    armor = db.Column(db.Integer(4))
    moveSpeed = db.Column(db.Float(120))
    BaseAttackTime = db.Column(db.Float(120))
    CastingAnimationPoint = db.Column(db.Float(120))
    CastingAnimationBackswing = db.Column(db.Float(120))
    attackAnimationPoint = db.Column(db.Float(120))
    attackAnimationBackswing = db.Column(db.Float(120))
    attackRangeValue = db.Column(db.Float(120))
    attackRangeType = db.Column(db.Float(120))
    MissileSpeed = db.Column(db.Float(120))
    introduction = db.Column(db.String(120))
    background = db.Column(db.String(120))
    SightRangeDay = db.Column(db.Float(120))
    SightRangeNight = db.Column(db.Float(120))
    SightRange = db.Column(db.Float(120))

    def __repr__(self):
        return '<Hero %r>' % (self.name + ' - ' + self.surname)