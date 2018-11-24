def ud(bot, update):
	from requests import get

	from chats_data import chats_data
	msg = update.message
	chat_id = msg.chat_id

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('ud', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /ud plugin is disabled. You can enable it using `/enable ud` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	msg_list = msg.text.strip().split(' ', 1)
	replied_msg = msg.reply_to_message

	if len(msg_list) == 2:
		word = msg_list[1].lower()
	elif replied_msg:
		word = replied_msg.text
	else:
		bot.send_message(chat_id = update.message.chat_id,
						 text = '*Format:*\n/ud _word_', 
						 parse_mode = 'Markdown', 
						 reply_to_message_id = update.message.message_id)
		return

	url = f'http://api.urbandictionary.com/v0/define?term={word}'

	response = get(url)
	data = response.json()
	
	if data['list']:
		first_answer = data['list'][0]

		heading = first_answer['word']
		definition = first_answer['definition']
		example = first_answer['example']

		reply = f"*{heading}*\n\n{definition}\n\n_{example}_"
		bot.send_message(chat_id = chat_id,
						 text = reply,
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
	else:
		bot.send_message(chat_id = update.message.chat_id,
						 text = 'No entry found.',
						 reply_to_message_id = update.message.message_id)
