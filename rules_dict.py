def load():
	from pickle import load
	rules_dict = {}
	rules_db = open('rules.db', 'rb')
	try:
		rules_dict = load(rules_db)
		return rules_dict
	except:
		return {}

rules_dict = load()