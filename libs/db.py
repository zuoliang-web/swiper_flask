
from flask_sqlalchemy import SQLAlchemy
from libs.orm import Query

db = SQLAlchemy(query_class=Query)
