def reminder(bot, update, job_queue):
	#from telegram.ext import Updater

	#updater = Updater(token="698907268:AAGQE2j1nGV1vWzYeiANn8x_G7U6IWiilZY") 
	#j = updater.job_queue

	msg = update.message
	chat_id = msg.chat_id

	user = bot.get_chat_member(chat_id = chat_id , user_id = msg.from_user.id)['status']

	if user in ['administrator', 'creator']:
		text = msg.text.split(" ",1)
		if len(text)>1:
			text = text[1].split(" ",1)
			if len(text)>1:
				time = int(text[0])
				text = text[1] 
				bot.send_message(chat_id = chat_id, text = f"Set a reminder for {time} seconds", reply_to_message_id = msg.message_id)
				def send_reminder(bot , job_queue):
					bot.send_message(chat_id = chat_id, text = text)
				job = job_queue.run_once(send_reminder, time)
			else:
				bot.send_message(chat_id = msg.chat_id, 
							 text = "*Format:*\n_/reminder time (in seconds) text_", 
							 reply_to_message_id = msg.message_id,
							 parse_mode = 'Markdown')
		else:
			bot.send_message(chat_id = msg.chat_id, 
							 text = "*Format:*\n_/reminder time (in seconds) text_", 
							 reply_to_message_id = msg.message_id,
							 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = msg.chat_id, 
							 text = "Fuck off, you aren't admin.", 
							 reply_to_message_id = msg.message_id,
							 parse_mode = 'Markdown')
