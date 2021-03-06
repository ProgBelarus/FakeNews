from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.auth.models import User


def email_exists(form, field):
    email = User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')


class RegistrationForm(FlaskForm):
    name = StringField('Name (As per MTurk regulations, DO NOT ENTER your ACTUAL name. MAKE IT UP.)', validators=[DataRequired(), Length(3, 15, message='between 3 to 15 characters')])
    email = StringField('E-mail (As per MTurk regulations, DO NOT ENTER your ACTUAL email address. MAKE IT UP, it should be of the form something@somethingelse.com )', validators=[DataRequired(), Email(), email_exists])
    password = PasswordField('Password', validators=[DataRequired(), Length(5), EqualTo('confirm', message='password must match')])
    confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    consent = StringField('I Consent to the Form Linked Above:',
                          validators=[DataRequired(message='You may not proceed without consenting '
                                                           'to the form linked above')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    stay_loggedin = BooleanField('stay logged-in')
    submit = SubmitField('LogIn')