import requests 
from times import d

def weather(bot, update):
	msg = update.message
	chat_id = msg.chat_id

	text = msg.text.split(' ',1)
	if len(text)>1:
		place = text[1]

		key = "fe35b3d7dc4f24468b3b376776035cfd"
		url = f"http://api.openweathermap.org/data/2.5/weather?id=524901&APPID={key}&q={place}"

		if not place.lower() in d.keys():

			response = requests.get(url)
			data = response.json()

			if data['cod'] != "404":
				temp_K = data['main']['temp']
				weather = data['weather'][0]['description'].capitalize()
				temp_C = temp_K-273
				temp_F = ((9*temp_C)/5)+32
				temp_C = round(temp_C, 2)
				temp_F = round(temp_F, 2)
				name = data['name']
				bot.send_message(chat_id = chat_id, text = f"`Place : {name}\nTemp : {temp_C}°C | {temp_F}F\nWeather : {weather}`", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
			else:
				bot.send_message(chat_id = chat_id, text = "No entries found.", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
		else:
			bot.send_message(chat_id = chat_id, text = "Please enter a city.", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
	else:
		bot.send_message(chat_id = chat_id, text = "*Format:*\n_/weather place_", parse_mode = "Markdown", reply_to_message_id = msg.message_id)

