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
    attackRangeType = db.Column(db.String(10))
    missileSpeed = db.Column(db.String(10))
    introduction = db.Column(db.String(120))
    background = db.Column(db.String(120))
    sightRangeDay = db.Column(db.Float(4))
    sightRangeNight = db.Column(db.Float(4))

    @property
    def serialize(self):
        """Return Hero data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'gainStrenght': self.gainStrength,
            'baseStrenght': self.baseStrength,
            'gainAgility': self.gainAgility,
            'baseAgility': self.baseAgility,
            'gainIntelligence': self.gainIntelligence,
            'baseIntelligence': self.baseIntelligence,
            'affiliation': self.affiliation,
            'damageMin': self.damageMin,
            'damageMax': self.damageMax,
            'armor': self.armor,
            'moveSpeed': self.moveSpeed,
            'castingAnimationPoint': self.castingAnimationPoint,
            'castingAnimationBackswing': self.castingAnimationBackswing,
            'attackAnimationPoint': self.attackAnimationPoint,
            'attackAnimationBackswing': self.attackAnimationBackswing,
            'attackRangeValue': self.attackRangeValue,
            'attackRangeType': self.attackRangeType,
            'sightRangeDay': self.sightRangeDay,
            'sightRangeNight': self.sightRangeNight
        }
