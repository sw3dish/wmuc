from wmuc import app
from wmuc.forms import LoginForm
from flask import render_template, request, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for username="%s", password="%s", remember_me="%s"' %
                (form.username.data, form.password.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html',
                            title="Log in",
                            form=form)

@app.route('/logout')
def logout():
    return None
