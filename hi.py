from peewee import *
from pyrogram import Client

db = SqliteDatabase('database.db')

class Members(Model):
	id = CharField()
	username = CharField()
	is_bot = BooleanField()
	first_name = CharField()
	


	class Meta : 
		database = db

db.connect()
db.create_tables([Members,])



app = Client('mosi34',api_hash='c2b827f39d1323302a587bdbc2463eb9',api_id='6728348')
target = "pyrogramchat"  # Target channel/supergroup

with app:
    for member in app.iter_chat_members(target):
        temp = Members.create(id=member.user.id,username=(member.user.username or ''),is_bot=member.user.is_bot,first_name=member.user.first_name)

temp = Members.get()
print (temp)