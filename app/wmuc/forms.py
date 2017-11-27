from flask_wtf import Form
from wmuc.models.user import User
from wtforms import StringField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(6, 64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])
    remember_me = BooleanField('Remember me', default=False)


class RegistrationForm(Form):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(6, 64),
        Regexp(
            '^[A-Za-z][A-Za-z0-9_.]*$',
            0,
            'Usernames must have only letters, '
            'numbers, dots or underscores'
        )
    ])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 128)])

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')


# Form for single user
class AddUserForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired()])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
