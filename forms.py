from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms import DateTimeLocalField
from wtforms.validators import DataRequired, Regexp, ValidationError, Email, Length, EqualTo

from models import User

def name_exists(form, field):
	if User.select().where(User.username == field.data).exists():
		raise ValidationError('User with this name already exists.')

def email_exists(form,field):
	if User.select().where(User.email == field.data).exists():
		raise ValidationError('User with this email already exists.')

class RegisterForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Regexp(
				r'^[a-zA-Z0-9_]+$',
				message = ("Username should be one word, letters, numbers and underscores only.")
				),
			name_exists
		])

	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email(),
			email_exists
		])

	password = PasswordField(
		'Password',
		validators=[
			DataRequired(),
			Length(min=2),
			EqualTo('password2', message = 'Passwords must match')
		])
	password2 = PasswordField(
		'Confirm Password',
		validators=[DataRequired()
		])
	first_name = StringField(
		'First Name',
		validators=[DataRequired()
		])
	last_name = StringField(
		'Last Name',
		validators=[DataRequired()
		])
	current_company = StringField(
		'Current Company',
		validators=[
		])
	current_role = StringField(
		'Current Role',
		validators=[
		])
	skills = StringField(
		'Skills',
		validators=[
		])
	description = StringField(
		'Description',
		validators=[
		])



class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class PostForm(FlaskForm):
	content = TextAreaField("Session Details", validators = [DataRequired()])
	timing = DateTimeLocalField('DatePicker',format='%Y-%m-%dT%H:%M')
