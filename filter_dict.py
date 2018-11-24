def load():
	from pickle import load
	filter_dict = {}
	filter_db = open('filter.db', 'rb')
	try:
		filter_dict = load(filter_db)
		return filter_dict
	except:
		return {}

filter_dict = load()