def msg_text(bot, update, user_data, job_queue):
	from filters import check_filters
	check_filters(bot, update)
	from sed import sed
	sed(bot, update)
	from stats import stats_check
	stats_check(bot, update, job_queue)