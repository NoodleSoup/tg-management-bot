def load():
	from pickle import load
	warn_dict = {}
	warn_db = open('warn.db', 'rb')
	try:
		warn_dict = load(warn_db)
		return warn_dict
	except:
		return {}

warn_dict = load()