from connect1 import *
from peewee import *
from dic import *
def signup():
	username=input("Create username -")
	
	email=input("Enter email/phone no -")
	password=input("Enter password - ")

	exists=len(User.select().where(User.username==username))

	if exists == 0:
		User.create(username=username,password=password,email=email)
		print("Signed up successfully")

	else:
		print("Username already Exists")



def login():
		username=input("Enter name")
		


		user= User.select().where(User.username==username)
		if len(user):
			user=user[0]
			print("\n Login Successful!!!")
			facebook(user.email,user.password)

			
		else:
			print("User doesn't exists")
