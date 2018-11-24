def load():
	from pickle import load
	welcome_dict = {}
	welcome_db = open('welcome.db', 'rb')
	try:
		welcome_dict = load(welcome_db)
		return welcome_dict
	except:
		return {}

welcome_dict = load()