from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask import flash, redirect, url_for
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from cocktailMolotov.models import User
from flask_login import current_user


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user:
            raise ValidationError('That username is already taken.')
    
    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

