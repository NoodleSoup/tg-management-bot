import requests

def tts(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id
	
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('tts', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /tts plugin is disabled. You can enable it using `/enable tts` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	text = ''
	msg_list = msg.text.strip().split(' ', 1)
	if len(msg_list) > 1:
		text += msg_list[1].strip().replace('&', '')
	else:
		text += 'what?'

	key = '52dc0dd127cf41688047c8a10af4fbc0'
	url = f'http://api.voicerss.org/?key={key}&hl=en-us&src={text}'

	data = requests.get(url)
	audio_data = data._content
	audio = open('audio.mp3', 'wb')
	audio.write(audio_data)
	audio.close()
	audio = open('audio.mp3', 'rb')
	bot.send_voice(chat_id = msg.chat_id,
				   voice = audio,
				   reply_to_message_id = msg.message_id)
	audio.close()

def weeb(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id
	
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('weeb', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /weeb plugin is disabled. You can enable it using `/enable weeb` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return

	text = ''
	msg_list = msg.text.strip().split(' ', 1)
	if len(msg_list) > 1:
		text += msg_list[1].strip().replace('&', '')
	else:
		text += 'なに?'

	key = '52dc0dd127cf41688047c8a10af4fbc0'
	url = f'http://api.voicerss.org/?key={key}&hl=ja-jp&src={text}&r=-3'

	data = requests.get(url)
	audio_data = data._content
	audio = open('audio.mp3', 'wb')
	audio.write(audio_data)
	audio.close()
	audio = open('audio.mp3', 'rb')
	bot.send_voice(chat_id = msg.chat_id,
				   voice = audio,
				   reply_to_message_id = msg.message_id)
	audio.close()
