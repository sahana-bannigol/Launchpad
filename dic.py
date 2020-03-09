from peewee import *

db=SqliteDatabase('users.db')


class User(Model):
    username=CharField()
    password=CharField()
    email=TextField()
    

    class Meta:
        database=db
if __name__=="__main__":
	db.connect()
	db.create_tables([User])