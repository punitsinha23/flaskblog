from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # Custom validation for username
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()  # Add .first() here
        if user:
            raise ValidationError('Username is taken.')

    # Custom validation for email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()  # Add .first() here
        if user:
            raise ValidationError('Email is taken.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update profile picture' , validators =[FileAllowed(['jpg' , 'png'])])
    submit = SubmitField('Update Profile')


    # Custom validation for username
    def validate_username(self, username):
        if username.data != current_user.username:  
            user = User.query.filter_by(username=username.data).first() 
            if user:
                raise ValidationError('Username is taken.')

    # Custom validation for email
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()  
            if user:
                raise ValidationError('Email is taken.')
            
class PostForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])         
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('Post')