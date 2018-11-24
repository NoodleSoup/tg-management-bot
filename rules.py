def rules(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('rules', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /rules plugin is disabled. You can enable it using `/enable rules` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	from rules_dict import rules_dict

	if chat_id in rules_dict:
		chat_rules = rules_dict[chat_id]
		bot.send_message(chat_id = msg.chat_id, 
						 text = f"*Rules:*\n{chat_rules}",
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "_There are no rules set for this chat._",
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')

def setrules(bot, update):
	from chats_data import chats_data
	
	msg = update.message
	chat_id = update.message.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('rules', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /setrules plugin is disabled. You can enable it using `/enable rules` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	import pickle
	from rules_dict import rules_dict
	
	setter = bot.get_chat_member(chat_id, msg.from_user.id)['status']

	if setter in ["administrator","creator"]:
		msg_list = msg.text.split("\n", 1)
		if len(msg_list) > 1:
			rules = msg_list[1]
			
			rules_dict[chat_id] = rules

			with open('rules.db', 'wb') as rules_db:
				pickle.dump(rules_dict, rules_db)
			
			bot.send_message(chat_id = msg.chat_id, 
						 text = "Rules added!", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		else:
			bot.send_message(chat_id = msg.chat_id, 
						 text = "*Format:*\n/setrules\n_rule 1\nrule 2_", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
						 text = "Fuck off.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')