def add_save(bot, update):
	from chats_data import chats_data
	from save_dict import save_dict

	chat_id = update.message.chat_id
	msg = update.message.text

	user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']

	if update.message.chat_id in chats_data.keys(): 
		if chats_data[chat_id]['save'] == True:
			if user in ["administrator", "creator"]:
				if '-' in msg:
					msg_list = msg.split(' ', 1)[1].split('-', 1)
					save_name = msg_list[0].strip().lower()

					if msg_list[1]:
						response = msg_list[1].strip()

						if chat_id in save_dict.keys():
							if save_name not in save_dict[chat_id].keys():
								save_dict[chat_id][save_name] = response

								from pickle import dump
								save_db = open('save.db', 'wb')
								dump(save_dict, save_db)
								save_db.close()

								text = f'#{save_name} succesfully added'
								bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
							else:
								text = f'A save already exists by the name `{save_name}`'
								bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
						else:
							save_dict[chat_id] = {}
							save_dict[chat_id][save_name] = response

							from pickle import dump
							save_db = open('save.db', 'wb')
							dump(save_dict, save_db)
							save_db.close()

							text = f'#{save_name} succesfully added'
							bot.send_message(chat_id = update.message.chat_id, text = text, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
					else:
						bot.send_message(chat_id = update.message.chat_id, text = '*Format:*\n/save _save_\__name_ - _response_', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
				else:
					bot.send_message(chat_id = update.message.chat_id, text = '*Format:*\n/save _save_\__name_ - _response_', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = 'No.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		
def check_saves(bot, update):
	from chats_data import chats_data
	from save_dict import save_dict
	
	msg = update.message
	chat_id = msg.chat_id
	if chats_data.get(chat_id, None) and chats_data[chat_id].get('save', None):
		txt = msg.text.lower()
		if chat_id in save_dict.keys():
			for trigger in save_dict[chat_id].keys():
				if txt.startswith(f'#{trigger}'):
					bot.send_message(chat_id = chat_id, text = save_dict[chat_id][trigger], reply_to_message_id = msg.message_id)

def save_list(bot, update):
	from save_dict import save_dict
	from chats_data import chats_data
	chat_id = update.message.chat_id
	chat_title = update.message.chat.title

	if chats_data.get(chat_id, None) and chats_data[chat_id].get('save', None):
		if chat_id in save_dict.keys():
			if save_dict[chat_id]:
				msg = f'Saves for {chat_title}:\n'
				save_list = save_dict[chat_id].keys()
				for save_name in save_list:
					msg += f'`{save_name}`\n'
				bot.send_message(chat_id = update.message.chat_id, text = msg, parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = 'Saves have not been added yet. Use /save to add.', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		else:
				bot.send_message(chat_id = update.message.chat_id, text = 'Saves have not been added yet. Use /save to add', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
	
def remove_save(bot, update):
	from chats_data import chats_data
	from save_dict import save_dict
	chat_id = update.message.chat_id
	msg = update.message.text
	if chats_data.get(chat_id, None) and chats_data[chat_id].get('save', None):
		user = bot.get_chat_member(chat_id, update.message.from_user.id)['status']
		if user in ["administrator", "creator"]:
			msg_list = msg.strip().split(' ', 1)

			if len(msg_list) == 2:
				trigger = msg_list[1].lower().strip()
				if chat_id in save_dict.keys():
					if trigger in save_dict[chat_id].keys():
						del save_dict[chat_id][trigger]

						from pickle import dump
						save_db = open('save.db', 'wb')
						dump(save_dict, save_db)
						save_db.close()

						bot.send_message(chat_id = update.message.chat_id, text = f'Successfully deleted `{trigger}`', parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
					else:
						bot.send_message(chat_id = update.message.chat_id, text = "Such a save doesn't exist for your group.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
				else:
					bot.send_message(chat_id = update.message.chat_id, text = "Saves have not been added yet", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
			else:
				bot.send_message(chat_id = update.message.chat_id, text = "*Format:*\n/stop _save_\__name_", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)
		else:
			bot.send_message(chat_id = update.message.chat_id, text = "No.", parse_mode = 'Markdown', reply_to_message_id = update.message.message_id)