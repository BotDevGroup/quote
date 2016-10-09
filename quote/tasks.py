from marvinbot.core import get_adapter
from marvinbot.utils import get_message
from marvinbot.handlers import Filters, CommandHandler, MessageHandler
from celery.utils.log import get_task_logger
from celery import task
import requests
from api_key import api_key

log = get_task_logger(__name__)
adapter = get_adapter()
print(api_key)

def quote_movie(update, *args):
    response = requests.get('https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies', headers={
      "X-Mashape-Key": api_key,
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json"
    })
    r = response.json()
    adapter.bot.sendMessage(chat_id=update.message.chat_id,
                            text="_{quote}_ -- *{author}*".format(quote=r['quote'],
                                                                  author=r['author']),
                            parse_mode='Markdown')

def quote_famous(update, *args):
    response = requests.get('https://andruxnet-random-famous-quotes.p.mashape.com/?cat=famous', headers={
      "X-Mashape-Key": api_key,
      "Content-Type": "application/x-www-form-urlencoded",
      "Accept": "application/json"
    })
    r = response.json()
    adapter.bot.sendMessage(chat_id=update.message.chat_id,
                            text="_{quote}_ -- *{author}*".format(quote=r['quote'],
                                                                  author=r['author']),
                            parse_mode='Markdown')

def setup(new_adapter):
    global adapter
    adapter = new_adapter

    adapter.add_handler(CommandHandler('moviequote', quote_movie, call_async=True))
    adapter.add_handler(CommandHandler('famousquote', quote_famous, call_async=True))

