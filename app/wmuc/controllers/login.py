from wmuc import app, lm
from wmuc.forms import LoginForm
from wmuc.models.user import User
from flask import g, render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required


@app.route('/login', methods=['GET', 'POST'])
def login():
    # if there is an authenticated user
    if g.user is not None and g.user.is_authenticated:
        # redirect back home
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.is_correct_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startsWith('/'):
                next = url_for('home')
            flash('Valid login')
            return redirect(next)
        flash('Invalid username or password.')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.before_request
def before_request():
    g.user = current_user
