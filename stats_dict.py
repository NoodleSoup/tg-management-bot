def load():
	from pickle import load
	stats_dict = {}
	stats_db = open('stats.db', 'rb')
	try:
		stats_dict = load(stats_db)
		return stats_dict
	except:
		print("i go to except")
		return {}
stats_dict = load()


def clear(bot, job_queue):
	global stats_dict
	stats_dict = {}
	print("cleared")