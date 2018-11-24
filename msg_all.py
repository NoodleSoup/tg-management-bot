def msg_all(bot, update, user_data, job_queue):
	from welcome import welcome
	welcome(bot, update, user_data)
	from stats import stats_check
	try:
		stats_check(bot, update, job_queue)
	except:
		pass