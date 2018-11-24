def load():
	from pickle import load
	save_dict = {}
	save_db = open('save.db', 'rb')
	try:
		save_dict = load(save_db)
		return save_dict
	except:
		return {}

save_dict = load()