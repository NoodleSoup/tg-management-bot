import requests


def cat(bot, update):
    from chats_data import chats_data

    msg = update.message
    chat_id = msg.chat_id
    msg_id = msg.message_id

    if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('cat', None):
        bot.send_message(chat_id=msg.chat_id,
                         text="The /cat plugin is disabled. You can enable it using `/enable cat` or by /plugins.",
                         reply_to_message_id=msg.message_id,
                         parse_mode='Markdown')
        return

    url = "https://api.thecatapi.com/v1/images/search?size=med&mime_types=jpg&format=json&order=RANDOM&page=0&limit=1"

    api_key = "93d5063b-edb9-41da-b124-88409869b1ce"
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': api_key
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    try:
        image_url = data[0]['url']
        bot.send_photo(chat_id=chat_id,
                       photo=image_url,
                       reply_to_message_id=msg_id)
    except:
        bot.send_message(chat_id=msg.chat_id,
                         text="Something went wrong...",
                         reply_to_message_id=msg.message_id,
                         parse_mode='Markdown')

