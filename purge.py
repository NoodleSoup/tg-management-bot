def purge(bot, update):
    from chats_data import chats_data

    msg = update.message
    chat_id = msg.chat_id
    user_id = msg.from_user.id
    
    if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('purge', None):
        bot.send_message(chat_id = chat_id, 
                         text = "The /purge plugin is disabled. You can enable it using `/enable purge` or by /plugins.", 
                         reply_to_message_id = msg.message_id,
                         parse_mode = 'Markdown')
        return

    user = bot.get_chat_member(chat_id, user_id)

    if user['status'] != "member":
        msg_list = msg.text.split(' ', 1)

        try:
            purge_limit = int(msg_list[1])
            msg_id = msg.message_id

            for lim in range(1, purge_limit + 1):
                msg_to_delete = msg_id - lim

                try:
                    bot.delete_message(chat_id, msg_to_delete)
                except:
                    pass

            bot.send_message(chat_id = chat_id, 
                             text = "Purge complete.",
                             reply_to_message_id = msg_id)
        except:
            bot.send_message(chat_id = chat_id, 
                             text = "Format:\n/purge <number>",
                             reply_to_message_id = msg_id)
