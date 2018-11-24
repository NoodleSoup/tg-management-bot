import requests

def tl(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id
	
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('tl', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /tl plugin is disabled. You can enable it using `/enable tl` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	text = ''
	if msg.reply_to_message:
		text += msg.reply_to_message.text
	else:
		msg_list = msg.text.strip().split(' ', 1)
		if len(msg_list) > 1:
			text += msg_list[1].strip().replace('&', '').replace('_', '\_').replace('*', '\*').replace('`', '\`')

	key = 'trnsl.1.1.20180815T121640Z.bc4cfb1562d86525.5eb07ce8cdd7b0da3b541cdb67d788a7f0e7718a'
	url = f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={key}&text={text}&lang=en'

	response = requests.get(url)
	data = response.json()

	reply = ''
	
	if data['code'] == 502:
		reply += "Fuck off."
	elif data['code'] != 200:
		reply += f"Something went wrong, Error {data['code']}"
	else:
		reply_text = '\n'.join(data['text'])
		reply += f"*{data['lang']}:*\n{reply_text}"

	bot.send_message(chat_id = msg.chat_id, 
					 text = reply, 
					 reply_to_message_id = msg.message_id,
					 parse_mode = 'Markdown')