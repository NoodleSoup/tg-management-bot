import requests

def currency(bot, update):
	msg = update.message
	chat_id = msg.chat_id

	text = msg.text.split()
	if len(text)==5:
		amount = text[1]
		to_be_converted = text[2].upper()
		to_convert_to = text[4].upper()

		api_key = f"{to_be_converted}_{to_convert_to}"

		url = f"https://free.currencyconverterapi.com/api/v6/convert?q={api_key}&compact=ultra"

		response = requests.get(url)
		data = response.json()

		if data:
			returned_amount = data[api_key]
			try:
				needed_amount = round(int(amount)*returned_amount,2)
				bot.send_message(chat_id = chat_id, text = f"*{needed_amount} {to_convert_to}*", parse_mode = "markdown", reply_to_message_id = msg.message_id)
			except:
				format_send(bot, update)
		else:
			format_send(bot, update)

def format_send(bot, update):
	msg = update.message
	chat_id = msg.chat_id
	bot.send_message(chat_id = chat_id, text = "*Format*\n_/convert 50 USD to INR_", parse_mode = "Markdown", reply_to_message_id = msg.message_id)


