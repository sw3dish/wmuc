from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object("wmuc.config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)
lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

import wmuc.controllers.about
import wmuc.controllers.home
import wmuc.controllers.login
import wmuc.controllers.register
import wmuc.controllers.admin
import wmuc.controllers.users


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
