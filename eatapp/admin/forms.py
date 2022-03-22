from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# --------------------- REGISTRATION FORM ------------------------
class RegistrationForm(FlaskForm):   # creates a class that inherits from Form
    # formfields and validators
    username = StringField('username', validators=[Length(min=4, max=25), DataRequired()])
    email = EmailField('email', validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), 
               Length(min=8) ])
    confirm_password = PasswordField('confirm password', validators=[DataRequired(), 
               Length(min=8), EqualTo('password', message='passwords must match')])
    submit = SubmitField('Signup')


# --------------------- LOGIN FORM ------------------------
class LoginForm(FlaskForm):   # creates a class that inherits from Form
    # formfields and validators
    email = EmailField('email', validators=[Email(), DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), 
               Length(min=8) ])
    remember = BooleanField('keep me logged in')
    submit = SubmitField('Login')