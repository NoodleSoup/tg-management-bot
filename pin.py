def pin(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('pin', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /pin plugin is disabled. You can enable it using `/enable pin` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	user = bot.get_chat_member(chat_id = chat_id, user_id = msg.from_user.id)['status']

	if user in ["administrator", "creator"]:
		try:
			bot.pin_chat_message(chat_id = chat_id, message_id = msg.reply_to_message.message_id, disable_notification = True)
		except:
			bot.send_message(chat_id = chat_id, text = "Couldn't pin message. Maybe I am not admin..", reply_to_message_id = msg.message_id)
	else:
		bot.send_message(chat_id = chat_id, text = "Fuck off, you aren't admin.", reply_to_message_id = msg.message_id)
