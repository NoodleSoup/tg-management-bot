def welcome(bot, update, user_data):
	from welcome_dict import welcome_dict
	from chats_data import chats_data
	
	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('welcome', None):
		return

	reply_markup = []

	if msg.new_chat_members:
		user_name = msg.new_chat_members[0]['username']
		if "_" in user_name:
			user_name = user_name.replace("_","\_")

		if chat_id in welcome_dict.keys():
			from telegram import InlineKeyboardMarkup, InlineKeyboardButton

			reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Rules", url = f't.me/maki_management_bot?start=rules_{chat_id}')]])
			text = welcome_dict[chat_id]
			bot.send_message(chat_id = msg.chat_id, 
					 text = text, 
					 reply_to_message_id = msg.message_id, reply_markup = reply_markup)
		else:
			bot.send_message(chat_id = msg.chat_id, 
						 text = f"@{user_name} Okairi motherfucker", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown', reply_markup = reply_markup)

def setwelcome(bot, update):
	import pickle
	from welcome_dict import welcome_dict
	from chats_data import chats_data

	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('welcome', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /setwelcome plugin is disabled. You can enable it using `/enable rules` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

	if setter in ["administrator", "creator"]:
		msg_list = msg.text.split(" ", 1)
		if len(msg_list) > 1:
			welcome_text = msg_list[1]
			
			welcome_dict[chat_id] = welcome_text
			with open('welcome.db', 'wb') as welcome_db:
				pickle.dump(welcome_dict, welcome_db)
			
			bot.send_message(chat_id = msg.chat_id, 
						 text = "Welcome message added added!", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		else:
			bot.send_message(chat_id = msg.chat_id, 
						 text = "*Format:*\n/setwelcome _welcome message_", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "Fuck off.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')