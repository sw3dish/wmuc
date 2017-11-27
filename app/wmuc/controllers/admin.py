from wmuc import app, db
from wmuc.forms import AddUserForm
from wmuc.email import send_email
from wmuc.models.user import User
from wmuc.models.role import Role
from flask import render_template, flash, redirect, url_for
from flask_login import login_required


@app.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')


@app.route('/admin/users/manage')
@login_required
def admin_users_manage():
    return render_template('admin_users')


@app.route('/admin/users/add/single', methods=['GET', 'POST'])
@login_required
def admin_users_add_single():
    form = AddUserForm()
    if form.validate_on_submit():
        # create a user in the database with the name and email
        user = User(
            name=form.name.data,
            email=form.email.data
        )
        db.session.add(user)
        db.session.commit()
        # generate a token and send it to the specified email
        token = user.generate_registration_token()
        send_email(
            form.email.data,
            "Register for an Account",
            "email/register",
            user=user,
            token=token)
        flash('Invitation sent to %s' % (form.name.data))
        return redirect(url_for('admin_users_add_single'))
    return render_template('admin_users_add_single.html', form=form)


@app.route('/admin/users/add/bulk')
@login_required
def admin_users_add_bulk():
    return render_template('admin_users_add_bulk.html')
