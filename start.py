def start(bot, update):
	from rules_dict import rules_dict

	chat_id = update.message.chat_id
	chat_title = update.message.chat.title
	if chat_id == update.message.from_user.id:
		text = update.message.text.split(" ",1)
		if len(text)>1:
			text = text[1].split("_",1)
			if text[0] == "rules" and len(text) > 1:
				chat_id = int(text[1])
				if chat_id in rules_dict.keys():
					bot.send_message(chat_id = update.message.chat_id, text = f"Rules for {chat_title}:\n{rules_dict[chat_id]}")
				else:
					bot.send_message(chat_id = update.message.chat_id, text = "This group doesnt have rules set.")
		else:
			bot.send_message(chat_id = update.message.chat_id, text = "Hi, I'm maki bot.")
	else:
		bot.send_message(chat_id = update.message.chat_id, text = "Hi, I'm maki bot.")


