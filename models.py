"""
Before Starting Package needed to be installed
1) pip install flask
2) pip install peewee
3) pip install flask-login
4) pip install flask-bcrypt (It uses the blue fish cipher)
5) pip install flask-wtf
"""
import datetime

from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
"""Flask have an ecosystem where package gets installed to this ext(external area)
module. and inside of that we get the package.
Read About UserMixin - 'http://flask-login.readthedocs.org/en/latest/#your-user-class'
"""

from peewee import *

DATABASE = SqliteDatabase('social.db')

class User(UserMixin, Model):
	"""Parent class can be more than one"""
	username = CharField(unique = True)
	email = CharField(unique = True)
	password = CharField(max_length = 100)
	joined_at = DateTimeField(default = datetime.datetime.now)
	first_name = CharField(max_length = 100)
	last_name = CharField(max_length = 100)
	skills = CharField()
	rating = FloatField()
	description = CharField()
	current_role = CharField()
	current_company = CharField()
	is_admin = BooleanField(default = False)

	class Meta:
		database = DATABASE
		order_by = ('-joined_at',)

	def get_posts(self):
		return Post.select().where(Post.user == self)

	def get_stream(self):
		return Post.select().where(
			(Post.user << self.following()),
			(Post.user == self)
			)

	def following(self):
		"""The users we are following"""
		return(
			User.select().join(
				Relationship, on=Relationship.to_user
				).where(
					Relationship.from_user == self
				)
			)

	def followers(self):
		"""Users Following the current user"""
		return(
			User.select().join(
				Relationship, on=Relationship.from_user
				).where(
					Relationship.to_user == self
				)
			)

	@classmethod
	def create_user(cls, username, email, password, first_name, last_name, 
	current_company = "", current_role= "", skills = "", description="",
	admin=False):
		"""cls here is being user. so cls.create is kind of user.create"""
		try:
			with DATABASE.transaction():
				cls.create(
					username = username,
					email = email,
					password = generate_password_hash(password),
					first_name = first_name,
					last_name = last_name,
					current_company = current_company,
					current_role = current_role,
					skills = skills,
					description = description,
					is_admin = admin
					)
		except IntegrityError:
			raise ValueError("User already exists")


class Post(Model):
	timestamp = DateTimeField(default = datetime.datetime.now)
	user = ForeignKeyField(
		User,
		related_name = 'posts'
	)
	content = TextField()
	timing = DateField()

	class Meta:
		database = DATABASE
		order_by = ('-timestamp',)

class Relationship(Model):
	from_user = ForeignKeyField(User, related_name='relationships')
	to_user = ForeignKeyField(User, related_name='related_to')

	class Meta:
		database = DATABASE
		indexes = (
				(('from_user','to_user'), True),
			)

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Post, Relationship], safe = True)
	DATABASE.close()
