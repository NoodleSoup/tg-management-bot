def admins(bot, update):
	from chats_data import chats_data
	chat_id = update.message.chat_id
	msg = update.message
	chat_title = msg.chat.title
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('admin list', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /admins plugin is disabled. You can enable it using `/enable admin list` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	text = f"*Admins for {chat_title}:*\n"
	for admin in bot.getChatAdministrators(chat_id = chat_id):
		if not admin.user.is_bot:
			username = admin.user.username.replace("_","\_")
			text += f"@{username}\n"
	bot.send_message(chat_id = chat_id, text = text, parse_mode= "Markdown")