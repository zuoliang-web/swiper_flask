from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import session
from flask_sqlalchemy.__init__ import BaseQuery

from .models import User
from .models import Profile
from user import logics
from main import app
from libs.http import render_json
from common import code_status
from libs.db import db


user_bp = Blueprint('user', import_name='user' )

user_bp.template_folder = './templates'


# 发送短信验证码
@user_bp.route('/send_mes',methods=('GET','POST'))
def send_mes():
    if request.method == 'POST':
        phone = request.form.get('phone')
        code_key = str(code_status.SENDMES_KEY % phone)
        if session.get(code_key):
            return render_json({'code':'1000'})
        msg = logics.send_mes(phone)
        if msg:
            return render_json({'code':'ok'})
        else:
            return render_json({'code':'1001'})


# 注册/登录
@user_bp.route('/register',methods=('GET','POST'))
def register():
    if request.method == 'POST':
        phone = request.form.get('phone')
        code = request.form.get('code')

        code_key =  code_status.SENDMES_KEY % phone
        print(code_key)
        code_token = session.get(code_key)
        print(code_token)
        if code_token and code_token == code:
            user = User(phone=phone,name=phone)
            db.session.add(user)
            db.session.commit()
            session['uid'] = user.id
            return render_json({'code':'OK'})
    else:
        return render_json({'code':'1002'})


@user_bp.route('/get_profile')
def get_profile():
    if request.method == 'GET':
        user = User.query.get_or_create(db.session,User,id=request.uid)
        return render_json({'code':'ok','data':user.name})


# 设置个人信息
@user_bp.route('/set_profile',methods=('GET','POST'))
def set_profile():
    if request.method == 'POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        location = request.form.get('location')
        birthday = request.form.get('birthday')
        min_distance = request.form.get('min_distance')
        max_distance = request.form.get('max_distance')
        min_dating_age = request.form.get('min_dating_age')
        max_dating_age = request.form.get('max_dating_age')
        
        
        # 更新user数据
        user = User.query.filter_by(id=request.uid).first()
        user.name = name
        user.phone = phone
        user.birthday = birthday
        user.gender = gender
        user.location = location

        # 更新profile数据
        profile = Profile.query.filter_by(id=request.uid).first()
        if profile:
            profile.location = location
            profile.dating_sex = dating_sex
            profile.min_distance = min_distance
            profile.max_distance = max_distance
            profile.min_dating_age = min_dating_age
            profile.max_dating_age = max_dating_age
        else:
            profile = Profile(id=request.uid,location=location,dating_sex=gender,
                                min_distance=min_distance,max_distance=max_distance,
                                min_dating_age=min_dating_age,max_dating_age=max_dating_age,
                                )
            db.session.add(profile)

        db.session.commit()

        return render_json({'code':'OK'})
        
    