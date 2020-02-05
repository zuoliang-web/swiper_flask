from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import session

from .models import User
from user import logics
from main import app
from libs.http import render_json
from common import code_status
from libs.db import db


user_bp = Blueprint('user', import_name='user' )

user_bp.template_folder = './templates'




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
