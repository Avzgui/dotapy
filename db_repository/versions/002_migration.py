from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
hero = Table('hero', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('surname', VARCHAR(length=120)),
    Column('MainStats', VARCHAR(length=120)),
    Column('baseAgility', FLOAT),
    Column('baseStrength', FLOAT),
    Column('baseIntelligence', FLOAT),
    Column('gainAgility', FLOAT),
    Column('gainStrength', FLOAT),
    Column('gainIntelligence', FLOAT),
    Column('affiliation', VARCHAR(length=50)),
    Column('damageMin', INTEGER),
    Column('damageMax', INTEGER),
    Column('armor', INTEGER),
    Column('moveSpeed', FLOAT),
    Column('BaseAttackTime', FLOAT),
    Column('CastingAnimationPoint', FLOAT),
    Column('CastingAnimationBackswing', FLOAT),
    Column('attackAnimationPoint', FLOAT),
    Column('attackAnimationBackswing', FLOAT),
    Column('attackRangeValue', FLOAT),
    Column('attackRangeType', FLOAT),
    Column('MissileSpeed', FLOAT),
    Column('introduction', VARCHAR(length=120)),
    Column('background', VARCHAR(length=120)),
    Column('SightRangeDay', FLOAT),
    Column('SightRangeNight', FLOAT),
    Column('SightRange', FLOAT),
)

hero = Table('hero', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('surname', String(length=120)),
    Column('mainStats', String(length=120)),
    Column('baseAgility', Float(precision=4)),
    Column('baseStrength', Float(precision=4)),
    Column('baseIntelligence', Float(precision=120)),
    Column('gainAgility', Float(precision=120)),
    Column('gainStrength', Float(precision=120)),
    Column('gainIntelligence', Float(precision=120)),
    Column('affiliation', String(length=50)),
    Column('damageMin', Integer),
    Column('damageMax', Integer),
    Column('armor', Integer),
    Column('moveSpeed', Float(precision=120)),
    Column('baseAttackTime', Float(precision=120)),
    Column('castingAnimationPoint', Float(precision=120)),
    Column('castingAnimationBackswing', Float(precision=120)),
    Column('attackAnimationPoint', Float(precision=120)),
    Column('attackAnimationBackswing', Float(precision=120)),
    Column('attackRangeValue', Float(precision=120)),
    Column('attackRangeType', Float(precision=120)),
    Column('missileSpeed', Float(precision=120)),
    Column('introduction', String(length=120)),
    Column('background', String(length=120)),
    Column('sightRangeDay', Float(precision=120)),
    Column('sightRangeNight', Float(precision=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['hero'].columns['BaseAttackTime'].drop()
    pre_meta.tables['hero'].columns['CastingAnimationBackswing'].drop()
    pre_meta.tables['hero'].columns['CastingAnimationPoint'].drop()
    pre_meta.tables['hero'].columns['MainStats'].drop()
    pre_meta.tables['hero'].columns['MissileSpeed'].drop()
    pre_meta.tables['hero'].columns['SightRange'].drop()
    pre_meta.tables['hero'].columns['SightRangeDay'].drop()
    pre_meta.tables['hero'].columns['SightRangeNight'].drop()
    post_meta.tables['hero'].columns['baseAttackTime'].create()
    post_meta.tables['hero'].columns['castingAnimationBackswing'].create()
    post_meta.tables['hero'].columns['castingAnimationPoint'].create()
    post_meta.tables['hero'].columns['mainStats'].create()
    post_meta.tables['hero'].columns['missileSpeed'].create()
    post_meta.tables['hero'].columns['sightRangeDay'].create()
    post_meta.tables['hero'].columns['sightRangeNight'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['hero'].columns['BaseAttackTime'].create()
    pre_meta.tables['hero'].columns['CastingAnimationBackswing'].create()
    pre_meta.tables['hero'].columns['CastingAnimationPoint'].create()
    pre_meta.tables['hero'].columns['MainStats'].create()
    pre_meta.tables['hero'].columns['MissileSpeed'].create()
    pre_meta.tables['hero'].columns['SightRange'].create()
    pre_meta.tables['hero'].columns['SightRangeDay'].create()
    pre_meta.tables['hero'].columns['SightRangeNight'].create()
    post_meta.tables['hero'].columns['baseAttackTime'].drop()
    post_meta.tables['hero'].columns['castingAnimationBackswing'].drop()
    post_meta.tables['hero'].columns['castingAnimationPoint'].drop()
    post_meta.tables['hero'].columns['mainStats'].drop()
    post_meta.tables['hero'].columns['missileSpeed'].drop()
    post_meta.tables['hero'].columns['sightRangeDay'].drop()
    post_meta.tables['hero'].columns['sightRangeNight'].drop()
