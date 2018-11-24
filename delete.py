def delete(bot, update):
	from time import sleep 

	msg = update.message
	chat_id = msg.chat_id

	deleter = bot.get_chat_member(chat_id = chat_id, user_id = msg.from_user.id)['status']

	if deleter in ['administrator','creator']:
		if msg.reply_to_message:
			occurance = bot.delete_message(chat_id = chat_id, message_id = msg.reply_to_message.message_id)
			if occurance:
				reason = msg.text.split(' ',1)
				if len(reason)>1:
					reason = reason[1]
					user_name = msg.reply_to_message.from_user.username.replace("_","\_")
					bot.send_message(chat_id = chat_id, text = f"@{user_name}'s *Message deleted.\nReason:* _{reason}_", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
					bot.delete_message(chat_id = chat_id, message_id = msg.message_id)

				else:
					sent_message = bot.send_message(chat_id = chat_id, text = f"*Message deleted.*", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
					bot.delete_message(chat_id = chat_id, message_id = msg.message_id)
					sleep(2)
					bot.delete_message(chat_id = chat_id, message_id = sent_message.message_id)
			else:
				bot.send_message(chat_id = chat_id, text = f"Couldn't delete message. Maybe I'm not admin...", reply_to_message_id = msg.message_id)
		else:
			bot.send_message(chat_id = chat_id, text = f"Reply to the message you want to delete.", reply_to_message_id = msg.message_id)
	else:
		bot.send_message(chat_id = chat_id, text = "Fuck off, you aren't admin.", reply_to_message_id = msg.message_id)

