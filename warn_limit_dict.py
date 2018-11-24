def load():
	from pickle import load
	warn_limit_dict = {}
	warn_limit_db = open('warn_limit.db', 'rb')
	try:
		warn_limit_dict = load(warn_limit_db)
		return warn_limit_dict
	except:
		return {}

warn_limit_dict = load()