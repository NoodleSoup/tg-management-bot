plugin_status_to_emoji =  {True : '✅', False : '❌', None : '❌'}

def plugins_keyboard(chats_data, chat_id, chat_title, plugins_list):
	from telegram import InlineKeyboardMarkup, InlineKeyboardButton

	plugin_buttons = []

	for i in range(0, len(plugins_list), 2):
		plugin1 = plugins_list[i]

		plugin2 = None
		if not i == len(plugins_list) - 1:
			plugin2 = plugins_list[i+1]

		button_line = []

		button_emoji = plugin_status_to_emoji[chats_data[chat_id].get(plugin1, None)]
		button_line.append(InlineKeyboardButton(f"{button_emoji}{plugin1}", 
			 									callback_data = plugin1))
		if plugin2:
			button_emoji = plugin_status_to_emoji[chats_data[chat_id].get(plugin2, None)]
			button_line.append(InlineKeyboardButton(f"{button_emoji}{plugin2}", 
			 										callback_data = plugin2))

		plugin_buttons.append(button_line)

	keyboard = InlineKeyboardMarkup(plugin_buttons)
	return keyboard

def plugins_callback(bot, update, user_data):
	from telegram import InlineKeyboardMarkup, InlineKeyboardButton
	from chats_data import chats_data
	from plugins_list import plugins_list

	query = update.callback_query
	plugin_name = query.data
	user_id = query.from_user.id

	chat_id = user_data['chat_id']
	chat_title = user_data['chat_title']

	if plugin_name in chats_data[chat_id]:
		chats_data[chat_id][plugin_name] = not chats_data[chat_id][plugin_name]
	else:
		chats_data[chat_id][plugin_name] = True

	from pickle import dump
	chats_db = open('chats.db', 'wb')
	dump(chats_data, chats_db)
	chats_db.close()

	reply_markup = plugins_keyboard(chats_data, chat_id, chat_title, plugins_list)

	bot.edit_message_text(text = f"Plugins for {chat_title}:",
						  chat_id = query.message.chat_id,
						  message_id = query.message.message_id,
						  reply_markup = reply_markup)

def plugins(bot, update, user_data):
	msg = update.message
	chat_id = msg.chat_id

	user = bot.get_chat_member(chat_id, msg.from_user.id)
	if user['status'] == 'member':
		bot.send_message(chat_id = chat_id,
						 text = "Fuck off.",
						 reply_to_message_id = msg.message_id)
		return

	from telegram import InlineKeyboardMarkup, InlineKeyboardButton
	from chats_data import chats_data
	from plugins_list import plugins_list
	
	chat_title = update.message.chat.title
	user_data['chat_id'] = chat_id
	user_data['chat_title'] = chat_title

	if chat_id not in chats_data.keys():
		chats_data[chat_id] = {}

		for plugin_name in plugins_list:
			chats_data[chat_id][plugin_name] = True
			
		from pickle import dump
		chats_db = open('chats.db', 'wb')
		dump(chats_data, chats_db)
		chats_db.close()

	reply_markup = plugins_keyboard(chats_data, chat_id, chat_title, plugins_list)

	try:
		bot.send_message(chat_id = msg.from_user.id, 
						 text = f"Plugins for {chat_title}:",
						 reply_markup = reply_markup)
	except:
		bot.send_message(chat_id = chat_id,
						 text = "[Start me in pm](telegram.me/maki_management_bot) and try again.",
						 reply_to_message_id = msg.message_id,
						 parse_mode = "Markdown")