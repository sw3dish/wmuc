from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("wmuc.config")
db = SQLAlchemy(app)

import wmuc.database

import wmuc.controllers.about
import wmuc.controllers.home
import wmuc.controllers.login

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
