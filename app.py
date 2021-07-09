from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doadmin:vcb4maoqvs8cxdci@farmly-db-do-user-9235528-0.b.db.ondigitalocean.com:25060/farmly_app?sslmode=require'
db = SQLAlchemy(app)

from Controller import *

