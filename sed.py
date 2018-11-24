import re

def sed(bot, update):
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id
	
	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('sed', None):
		return

	if msg.text.startswith('s/'):
		if msg.reply_to_message:
			string = msg.reply_to_message.text or msg.reply_to_message.caption

			msg_list = msg.text.split('/')

			pattern = msg_list[1]
			repl = msg_list[2]

			result = re.sub(pattern, repl, string)

			reply = f"{result}" if result else "_\*empty message\*_"

			bot.send_message(chat_id = chat_id,
							 text = reply,
							 reply_to_message_id = msg.reply_to_message.message_id,
							 parse_mode = "Markdown")

