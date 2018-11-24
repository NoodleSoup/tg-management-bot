from telegram.ext import (Updater, MessageHandler, Filters, CommandHandler,
                          ConversationHandler, CallbackQueryHandler, RegexHandler)
import logging

from start import start
#help, commands
from plugins import plugins, plugins_callback

from msg_text import msg_text
from msg_all import msg_all

from welcome import setwelcome
from rules import rules, setrules
from admins import admins

from pin import pin
from ban import ban
from kick import kick
from warn import setwarn, warn, clearwarns #unwarn
from mute import mute, unmute
from purge import purge
from delete import delete

from save import add_save, save_list, remove_save
from filters import add_filter, filter_list, remove_filter
from ud import ud
from tl import tl
from tts import tts, weeb
from reminder import reminder

from cat import cat
from dog import dog
from youtube import youtube, mp3

from stats import stats, gstats
from stats_dict import clear
from time_until_12 import totaltime

from weather import weather
from times import times
from currency import currency

def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token="TOKEN")
 
    dispatcher = updater.dispatcher
    j = updater.job_queue

    start_handler = CommandHandler('start', start)

    plugins_handler = CommandHandler('plugins',
                                     plugins,
                                     pass_user_data=True)

    plugins_callback_handler = CallbackQueryHandler(plugins_callback,
                                                    pass_user_data=True)

    msg_text_handler = MessageHandler(Filters.text,
                                      msg_text,
                                      pass_user_data=True,
                                      pass_job_queue=True)

    msg_all_handler = MessageHandler(Filters.all,
                                     msg_all,
                                     pass_user_data=True,
                                     pass_job_queue=True)

    setwelcome_handler = CommandHandler('setwelcome', setwelcome)
    rules_handler = CommandHandler('rules', rules)
    setrules_handler = CommandHandler('setrules', setrules)
    
    warn_handler = CommandHandler('warn', warn)
    setwarn_handler = CommandHandler('setwarn', setwarn)
    clearwarn_handler = CommandHandler('clearwarns', clearwarns)

    kick_handler = CommandHandler('kick', kick)
    ban_handler = CommandHandler('ban', ban)
    pin_handler = CommandHandler('pin', pin)
    mute_handler = CommandHandler('mute', mute)
    unmute_handler = CommandHandler('unmute', unmute)
    delete_handler = CommandHandler('del', delete)
    purge_handler = CommandHandler('purge', purge)
    
    add_save_handler = CommandHandler('save', add_save)
    save_list_handler = CommandHandler('saves', save_list)
    remove_save_handler = CommandHandler('clear', remove_save)

    add_filter_handler = CommandHandler('filter', add_filter)
    filter_list_handler = CommandHandler('filters', filter_list)
    remove_filter_handler = CommandHandler('stop', remove_filter)

    admins_handler = CommandHandler('admins', admins)

    ud_handler = CommandHandler('ud', ud)
    tl_handler = CommandHandler('tl', tl)
    tts_handler = CommandHandler('tts', tts)
    weeb_handler = CommandHandler('weeb', weeb)

    reminder_handler = CommandHandler(['remind', 'reminder'],
                                      reminder,
                                      pass_job_queue=True)

    cat_handler = CommandHandler('cat', cat)
    dog_handler = CommandHandler('dog', dog)
    youtube_handler = CommandHandler('youtube', youtube)
    mp3_handler = CommandHandler('mp3', mp3)

    stats_handler = CommandHandler('stats', stats)
    gstats_handler = CommandHandler('gstats', gstats)

    job = j.run_repeating(clear, interval=86400, first=totaltime)

    weather_handler = CommandHandler('weather', weather)
    time_handler = CommandHandler('time', times)
    currency_handler = CommandHandler('convert', currency)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(plugins_handler)
    dispatcher.add_handler(plugins_callback_handler)
    dispatcher.add_handler(setwelcome_handler)
    dispatcher.add_handler(rules_handler)
    dispatcher.add_handler(setrules_handler)
    dispatcher.add_handler(warn_handler)
    dispatcher.add_handler(setwarn_handler)
    dispatcher.add_handler(clearwarn_handler)
    dispatcher.add_handler(kick_handler)
    dispatcher.add_handler(ban_handler)
    dispatcher.add_handler(mute_handler)
    dispatcher.add_handler(unmute_handler)
    dispatcher.add_handler(delete_handler)
    dispatcher.add_handler(purge_handler)
    dispatcher.add_handler(add_save_handler)
    dispatcher.add_handler(save_list_handler)
    dispatcher.add_handler(remove_save_handler)
    dispatcher.add_handler(add_filter_handler)
    dispatcher.add_handler(filter_list_handler)
    dispatcher.add_handler(remove_filter_handler)
    dispatcher.add_handler(admins_handler)
    dispatcher.add_handler(ud_handler)
    dispatcher.add_handler(tl_handler)
    dispatcher.add_handler(tts_handler)
    dispatcher.add_handler(weeb_handler)
    dispatcher.add_handler(reminder_handler)
    dispatcher.add_handler(pin_handler)
    dispatcher.add_handler(cat_handler)
    dispatcher.add_handler(dog_handler)
    dispatcher.add_handler(youtube_handler)
    dispatcher.add_handler(mp3_handler)
    dispatcher.add_handler(stats_handler)
    dispatcher.add_handler(gstats_handler)
    dispatcher.add_handler(weather_handler)
    dispatcher.add_handler(time_handler)
    dispatcher.add_handler(currency_handler)

    dispatcher.add_handler(msg_text_handler)
    dispatcher.add_handler(msg_all_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
