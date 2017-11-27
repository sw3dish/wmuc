from wmuc import app, db
from wmuc.models.user import User
from wmuc.forms import RegistrationForm
from flask import flash, redirect, url_for, render_template, g


@app.route('/register/<token>', methods=['GET', 'POST'])
def register(token):
    # make sure that there is no user logged in
    if g.user is None or not g.user.is_authenticated:
        user = User.register(token)
        if user is not None:
            form = RegistrationForm()
            if form.validate_on_submit():
                user.username = form.username.data
                user.password = form.password.data
                user.registered = True
                db.session.commit()
                flash('You can now login.')
                return redirect(url_for('login'))
            return render_template('register.html', form=form)
    flash('Invalid token')
    return redirect(url_for('home'))
