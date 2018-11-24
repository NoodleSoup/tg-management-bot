def stats_check(bot , update, job_queue):
	from stats_dict import stats_dict
	from chats_data import chats_data
	from global_stats import global_stats_dict
	from time import gmtime, strftime

	msg = update.message
	user = msg.from_user.id
	chat_id = update.message.chat_id
	user_object = msg.from_user

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('stats', None):
		return

	increment(stats_dict, chat_id, user_object)
	increment(global_stats_dict, chat_id, user_object)

	from pickle import dump
	stats_db = open('stats.db', 'wb')
	dump(stats_dict, stats_db)
	stats_db.close()

	global_stats_db = open('global_stats.db','wb')
	dump(global_stats_dict, global_stats_db)
	global_stats_db.close()

def stats(bot, update):
	from stats_dict import stats_dict
	from chats_data import chats_data

	msg = update.message
	chat_id = msg.chat_id
	chat_title = msg.chat.title

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('stats', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /stats plugin is disabled. You can enable it using `/enable stats` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return


	if chat_id in stats_dict.keys():
		if stats_dict[chat_id]:

			text = f"*Stats for {chat_title}:*\n"
			user_list, value_list = desc(stats_dict, chat_id)

			for index, user in enumerate(user_list, 0):
				if user != "total_messages" and "generated":
					percentage = round((value_list[index]/stats_dict[chat_id]['total_messages'])*100, 2)
					text += f"_{user.first_name} - {percentage}%_\n"
				if index == 9:
					break
			bot.send_message(chat_id = chat_id, text = f"{text}\n_Total messages - {stats_dict[chat_id]['total_messages']}_", reply_to_message_id = msg.message_id, parse_mode = "Markdown")
		else:
			bot.send_message(chat_id = chat_id, text = "No messages here yet.", reply_to_message_id = msg.message_id)
	else:
		bot.send_message(chat_id = chat_id, text = "No messages here yet.", reply_to_message_id = msg.message_id)

def gstats(bot, update):
	from chats_data import chats_data
	from global_stats import global_stats_dict
	from times import month_dict

	msg = update.message
	chat_id = msg.chat_id
	chat_title = msg.chat.title

	if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('stats', None):
		bot.send_message(chat_id = msg.chat_id, 
						 text = "The /stats plugin is disabled. You can enable it using `/enable stats` or by /plugins.", 
						 reply_to_message_id = msg.message_id,
						 parse_mode = 'Markdown')
		return
	if 'generated' in global_stats_dict[chat_id].keys():
		generated = global_stats_dict[chat_id]["generated"]
		generated = generated.split("-",2)
		year = generated[0]
		month = month_dict[int(generated[1])]
		date = generated[2]

		if int(date) % 10 == 3 and int(date)/10!=1:
				date = str(date) + "rd"
		elif int(date) % 10 == 2 and int(date)/10!=1:
				date = str(date) + "nd"
		elif int(date) %10 == 1 and int(date)/10!=1:
				date = str(date) + "st"
		else:
				date = str(date) + "th"

		text = f"Stats for {chat_title}:\nGenerated on {date} {month}, {year}.\n\n"
	else: #Means we are counting before i made generated. I implemented this shit on 19th August
		text = f'Stats for {chat_title}:\nGenerated on 19th August, 2018.\n\n'
	user_list, value_list = desc(global_stats_dict, chat_id)

	with open('stats.txt', 'w') as file:
		for index, user in enumerate(user_list, 0):
			if user != "total_messages" and "generated":
				messages = value_list[index]
				if messages == 1:
					messages = str(messages)+" message"
				else:
					messages = str(messages)+" messages."

				percentage = round((value_list[index]/global_stats_dict[chat_id]['total_messages'])*100, 2)
				text += f"{index+1}.{user.first_name} - {value_list[index]} [{percentage}%]\n"
		file.write(text)
	file = open('stats.txt', 'rb')
	bot.send_document(chat_id = msg.chat_id,
				   document = file,
				   reply_to_message_id = msg.message_id)
	file.close()

def desc(dicc, chat_id):
	#This sort gay. I'll change later
	dic = dicc #So that the ['generated'] value wont get deleted from actual dict, i made a copy. Or else it gives error because all other values int while this is string. Cant sort
	try:
		del dic[chat_id]['generated']
	except:
		pass
	keys = list(dic[chat_id].keys())
	values = list(dic[chat_id].values())
	values.sort(reverse = True)

	key_list = [] 
	value_list = []
	used_list = []

	for value in values:
		for key in keys:
			if key not in ["total_messages", "generated"] and key not in used_list:
				if dic[chat_id][key] == value:
					key_list.append(key)
					value_list.append(value)
					used_list.append(key)
	return key_list, value_list

def increment(dic, chat_id, user_object):
	from time import gmtime, strftime
	if chat_id not in dic.keys():
		dic[chat_id] = {}
		dic[chat_id]["generated"] = strftime("%Y-%m-%d", gmtime())
		dic[chat_id]['total_messages'] = 0
	if user_object not in dic[chat_id]:
		dic[chat_id][user_object] = 1
		dic[chat_id]['total_messages'] += 1
	else:
		dic[chat_id][user_object] += 1
		dic[chat_id]['total_messages'] += 1



