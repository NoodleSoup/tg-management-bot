def add_filter(bot, update):
	from chats_data import chats_data
	from filter_dict import filter_dict

	chat_id = update.message.chat_id
	msg = update.message.text

	user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']

	if update.message.chat_id in chats_data.keys(): 
		if chats_data[chat_id]['filters'] == True:
			if user in ["administrator", "creator"]:
				if '-' in msg:
					msg_list = msg.split(' ', 1)[1].split('-', 1)
					filter_name = msg_list[0].strip().lower()

					if msg_list[1]:
						response = msg_list[1].strip()

						if chat_id in filter_dict.keys():
							if filter_name not in filter_dict[chat_id].keys():
								filter_dict[chat_id][filter_name] = response

								from pickle import dump
								filter_db = open('filter.db', 'wb')
								dump(filter_dict, filter_db)
								filter_db.close()

								text = f'Filter `{filter_name}` succesfully added'
								bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
							else:
								text = f'A Filter already exists by the name `{filter_name}`'
								bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
						else:
							filter_dict[chat_id] = {}
							filter_dict[chat_id][filter_name] = response

							from pickle import dump
							filter_db = open('filter.db', 'wb')
							dump(filter_dict, filter_db)
							filter_db.close()

							text = f'Filter `{filter_name}` succesfully added'
							bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
					else:
						bot.send_message(chat_id = update.message.chat_id, text = '*Format:*\n/filter _filter_\__name_ - _response_', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
				else:
					bot.send_message(chat_id = update.message.chat_id, text = '*Format:*\n/filter _filter_\__name_ - _response_', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = 'Fuck off.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		else:
			bot.send_message(chat_id = update.message.chat_id, text = 'The /filter plugin is disabled. You can enable it using `/enable filters` or by /plugins.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)

def check_filters(bot, update):
	from chats_data import chats_data
	from filter_dict import filter_dict
	from re import search
	
	msg = update.message
	chat_id = msg.chat_id
	if chats_data.get(chat_id, None) and chats_data[chat_id].get('filters', None):
		txt = msg.text.lower()
		if chat_id in filter_dict.keys():
			for trigger in filter_dict[chat_id].keys():
				if search(rf"\b{trigger}\b", txt):
					bot.send_message(chat_id = chat_id, text = filter_dict[chat_id][trigger], reply_to_message_id = msg.message_id)

def filter_list(bot, update):
	from filter_dict import filter_dict
	from chats_data import chats_data
	chat_id = update.message.chat_id
	chat_title = update.message.chat.title

	if chats_data.get(chat_id, None) and chats_data[chat_id].get('filters', None):
		if chat_id in filter_dict.keys():
			if filter_dict[chat_id]:
				msg = f'Filters for {chat_title}:\n'
				filter_list = filter_dict[chat_id].keys()
				for filter_name in filter_list:
					msg += f'`{filter_name}`\n'
				bot.send_message(chat_id = update.message.chat_id, text = msg, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = 'Filters have not been added yet. Use /filter to add.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		else:
				bot.send_message(chat_id = update.message.chat_id, text = 'Filters have not been added yet. Use /filter to add', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
	else:
		bot.send_message(chat_id = update.message.chat_id, text = 'The /filters plugin is disabled. You can enable it using `/enable filters` or by /plugins.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)

def remove_filter(bot, update):
	from chats_data import chats_data
	from filter_dict import filter_dict
	chat_id = update.message.chat_id
	msg = update.message.text
	if chats_data.get(chat_id, None) and chats_data[chat_id].get('filters', None):
		user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']
		if user in ["administrator", "creator"]:
			msg_list = msg.strip().split(' ', 1)

			if len(msg_list) == 2:
				trigger = msg_list[1].lower().strip()
				if chat_id in filter_dict.keys():
					if trigger in filter_dict[chat_id].keys():
						del filter_dict[chat_id][trigger]

						from pickle import dump
						filter_db = open('filter.db', 'wb')
						dump(filter_dict, filter_db)
						filter_db.close()

						bot.send_message(chat_id = update.message.chat_id, text = f'Successfully deleted `{trigger}`', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
					else:
						bot.send_message(chat_id = update.message.chat_id, text = "Such a filter doesn't exist for your group.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
				else:
					bot.send_message(chat_id = update.message.chat_id, text = "Filters have not been added yet", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = "*Format:*\n/stop _filter_\__name_", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		else:
			bot.send_message(chat_id = update.message.chat_id, text = "Fuck off.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
	else:
		bot.send_message(chat_id = update.message.chat_id, text = "The /stop command is disabled. You can enable it using `/enable filters` or by /plugins.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
