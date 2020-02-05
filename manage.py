from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from main import app
from libs.db import db
from user.models import User

db.init_app(app)

manage = Manager(app)

migrate = Migrate(app,db)

manage.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manage.run()