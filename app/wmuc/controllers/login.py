from wmuc import app
from flask import render_template, url_for, request

@app.route('/login', methods=['POST'])
def login():
    return None

@app.route('/logout')
def logout():
    return None
