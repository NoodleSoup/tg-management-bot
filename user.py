def user(bot, update):
	from warn_dict import warn_dict
	from global_stats import global_stats_dict

	msg = update.message
	chat_id = update.message.chat_id

	if msg.reply_to_message:
		user = msg.reply_to_message.from_user
	else:
		user = msg.from_user
	first_name = user.first_name
	last_name = user.last_name 
	username = user.username.replace('_',"\_")
	if chat_id in warn_dict.keys():
		if user.id in warn_dict[chat_id].keys():
			warns = warn_dict[chat_id][user.id]
		else:
			warns = 0
	else:
		warns = 0
	user_id = user.id

	status = bot.get_chat_member(chat_id = chat_id, user_id = user.id)['status']

	if chat_id in global_stats_dict.keys():
		if user in global_stats_dict[chat_id].keys():
			total_messages = global_stats_dict[chat_id][user] 

	bot.send_message(chat_id = chat_id, text = f"*First name:* _{first_name}_\n*Last name:* _{last_name}_\n*Username:* @{username}\n*Number of warns:* _{warns}_\n*Status:* _{status}_\n*Total messages:* _{total_messages}_", parse_mode = "Markdown", reply_to_message_id = msg.message_id)