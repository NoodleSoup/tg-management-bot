def load():
	from pickle import load
	chats_dict = {}
	chats_db = open('chats.db', 'rb')
	try:
		chats_dict = load(chats_db)
		return chats_dict
	except:
		return {}

chats_data = load()