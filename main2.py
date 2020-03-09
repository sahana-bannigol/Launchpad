from dic import *
from connect1 import *
from peewee import *
from pos import *
db.connect()
conti=True
while True:
	print("*"*40)
	print("    Welcome to AutoFill for Facebook")
	print("*"*40)
	opt=input("Do you have an account in our database? Y/N\n")
	opt=opt.lower()
	if opt== "y":
		login()

	else:
		signup()
	f= int(input("To continue enter 1 "))
	if not f:
		exit()







