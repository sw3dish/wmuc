from wmuc import app
from flask import render_template


@app.route('/about/history')
def static_history():
    return render_template("history.html")


@app.route('/about/staff')
def static_staff():
    return render_template("staff.html")


@app.route('/about/get_involved')
def static_get_involved():
    return render_template("get_involved.html")


@app.route('/about/donate')
def static_donate():
    return render_template("donate.html")


@app.route('/submit/psa')
def static_submit_psa():
    return render_template("psa.html")


@app.route('/submit/music')
def static_submit_music():
    return render_template("music.html")
