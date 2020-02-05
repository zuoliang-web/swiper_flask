from flask import Flask
from flask import session
from libs.db import db


app = Flask(__name__)
#app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '\x17[\xb9\xd0\x9c\xa2\x03\xac\xce\x0f'  # 为session设置安全密钥 【flask独有的】


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ZLrourou0509!!!@localhost/swiper_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app) 

@app.route('/')
def main():
    return 'server is main'


if __name__ == '__main__':
    from user.api import user_bp
    app.register_blueprint(user_bp,url_prefix='/user') 
    app.run()