from sqlalchemy_utils.types.choice import ChoiceType

from libs.db import db


class User(db.Model):
    
    __tablename__ = 'user'

    genders=(
        (u'male',u'男性'),
        (u'female',u'女性')
    )

    locations = (
        (u'北京',u'北京'),
        (u'上海',u'上海'),
        (u'重庆',u'重庆'),
        (u'武汉',u'武汉'),
        (u'南京',u'南京'),
    )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, index=True)
    phone = db.Column(db.String(50))
    avatar = db.Column(db.String(100))
    gender = db.Column(ChoiceType(genders))
    location = db.Column(ChoiceType(locations))
    birthday = db.Column(db.Date,default='2000-01-01')

