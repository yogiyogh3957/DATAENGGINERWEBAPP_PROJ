from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import os

import os

app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:password@localhost:5432/fpldb"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "postgresql://postgres:password@localhost:5432/fpldb")
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db = SQLAlchemy(app)
from fplapp import routes