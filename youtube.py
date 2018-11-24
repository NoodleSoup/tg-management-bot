import requests
from pprint import pprint

def youtube(bot, update):
    from chats_data import chats_data

    msg = update.message
    chat_id = msg.chat_id
    msg_id = msg.message_id
    
    if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('youtube', None):
        bot.send_message(chat_id=msg.chat_id,
                         text="The /youtube plugin is disabled. You can enable it using `/enable youtube` or by /plugins.",
                         reply_to_message_id=msg_id,
                         parse_mode='Markdown')
        return

    msg_list = msg.text.split(' ', 1)[1].split()
    pprint(msg_list)
    for member in msg_list:
        member = member.lstrip('http://').lstrip('https://').lstrip('www.')

        if member.startswith('youtu.be/'):
            video_id = member[len('youtu.be/'):]
            if '?' in video_id:
                tags_index = video_id.index('?')
                video_id = video_id[:tags_index]
        elif member.startswith('youtube.com'):
            video_id = member[len('youtube.com/watch?v='):]
            if '&' in video_id:
                tags_index = video_id.index('&')
                video_id = video_id[:tags_index]
        else:
            continue

        url = f"https://api.unblockvideos.com/youtube_downloader?id={video_id}&selector=mp4"
        response = requests.get(url)
        data = response.json()

        if type(data) == type([]):
            video_url = data[0].get('url', None) 
            response = requests.get(video_url)
            video = response.content
            with open('video.mp4', 'wb') as video_file:
                video_file.write(video)
            with open('video.mp4', 'rb') as video_file:
                bot.send_video(chat_id=chat_id,
                               video=video_file,
                               reply_to_message_id=msg_id)
        else:
            bot.send_message(chat_id=chat_id,
                             text="Invalid url.",
                             reply_to_message_id=msg_id)

def mp3(bot, update):
    from chats_data import chats_data

    msg = update.message
    chat_id = msg.chat_id
    msg_id = msg.message_id
    
    if not chats_data.get(chat_id, None) or not chats_data[chat_id].get('youtube', None):
        bot.send_message(chat_id=msg.chat_id,
                         text="The /youtube plugin is disabled. You can enable it using `/enable youtube` or by /plugins.",
                         reply_to_message_id=msg_id,
                         parse_mode='Markdown')
        return

    msg_list = msg.text.split(' ', 1)[1].split()
    pprint(msg_list)
    for member in msg_list:
        member = member.lstrip('http://').lstrip('https://').lstrip('www.')

        if member.startswith('youtu.be/'):
            video_id = member[len('youtu.be/'):]
            if '?' in video_id:
                tags_index = video_id.index('?')
                video_id = video_id[:tags_index]
        elif member.startswith('youtube.com'):
            video_id = member[len('youtube.com/watch?v='):]
            if '&' in video_id:
                tags_index = video_id.index('&')
                video_id = video_id[:tags_index]
        else:
            continue
        print(video_id)
        url = f"http://www.convertmp3.io/fetch/?format=JSON&video=https://www.youtube.com/watch?v={video_id}&redirect=false"
        response = requests.get(url)

        print(response.content)
        try:
            data = response.json()
        except:
            bot.send_message(chat_id=chat_id,
                             text="Invalid url.",
                             reply_to_message_id=msg_id)
            continue

        audio_url = data.get('link', None)
        if audio_url:
            response = requests.get(audio_url)
            audio = response.content
            with open('audio.mp3', 'wb') as audio_file:
                audio_file.write(audio)
            with open('audio.mp3', 'rb') as audio_file:
                bot.send_audio(chat_id=chat_id,
                               audio=audio_file,
                               reply_to_message_id=msg_id)
        else:
            bot.send_message(chat_id=chat_id,
                             text="Invalid url.",
                             reply_to_message_id=msg_id)
