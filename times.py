import requests

month_dict = {1 : "January", 2: "February", 3 : "March", 4 : "April", 5 : "May", 6 : "June", 7 : "July", 8 : "August", 9 : "September", 10 : "October", 11 : "November", 12 : "December"}

#key = "BB3JGB5G0CZV"
#url = f"http://api.timezonedb.com/v2/list-time-zone?key={key}&format=json&country=NZ"

#response = requests.get(url)
#data = response.json()

def times(bot, update):
	msg = update.message
	chat_id = msg.chat_id

	text = msg.text.split(' ',1)
	if len(text)>1:
		place = text[1]

		try:
			find_time(bot, update, place, chat_id, msg)
		except:
			global d
			place = place.lower()
			if place in d.keys():
				place = d[place]
				print(place)
				try:
					find_time(bot, update, place, chat_id, msg)
				except:
					bot.send_message(chat_id = chat_id, text = "No entries found.", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
			else:
				bot.send_message(chat_id = chat_id, text = "No entries found.", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
	else:
		bot.send_message(chat_id = chat_id, text = "*Format:*\n_/weather city\n/weather country, city\n/country, state, city_", parse_mode = "Markdown", reply_to_message_id = msg.message_id)

d = {}
with open('country-list.csv') as fp:
    for line in fp:
	    countrylist = line.split(",")
	    d[countrylist[0].lower().replace("\"","")] = countrylist[1].replace("\"","").lower()

def find_time(bot, update, place, chat_id, msg):
		key = "dEcyzH7YEduBqGDwTmMQFWxwXd5jrH"
		url = f"https://www.amdoren.com/api/timezone.php?api_key={key}&loc={place}"


		response = requests.get(url)
		data = response.json()

		print(data)

		time = data['time'].split(" ",1)
		date = time[0]
		time = time[1]
		time_12 = time.split(":",1)
		if int(time_12[0]) >= 12:
			time = f"{str(int(time_12[0])-12)}:{time_12[1]} P.M"
		else:
			time += " A.M"
		timezone = data['timezone']
		offset = data['offset']/60

		if offset>0:
			offset = "+"+str(offset)

		month_data = date.split("-", 2)
		month = month_data[1]
		date = month_data[2]
		year = month_data[0]
		if int(date) % 10 == 3 and int(date)/10!=1:
			date = str(date) + "rd"
		if int(date) % 10 == 2 and int(date)/10!=1:
			date = str(date) + "nd"
		if int(date) %10 == 1 and int(date)/10!=1:
			date = str(date) + "st"
		else:
			date = str(date) + "th"

		month_name = month_dict[int(month)]

		bot.send_message(chat_id = chat_id, text = f"`{date} {month_name} {year}\nTime : {time}\nTimezone : {timezone} [{offset}]`", parse_mode = "Markdown", reply_to_message_id = msg.message_id)
