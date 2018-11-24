def load():
	from pickle import load
	global_stats_dict = {}
	global_stats_db = open('global_stats.db', 'rb')
	try:
		global_stats_dict = load(global_stats_db)
		return global_stats_dict
	except:
		print("I go to excpt in global")
		return {}
global_stats_dict = load()
