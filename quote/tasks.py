from marvinbot.core import get_adapter
from marvinbot.utils import get_message
from marvinbot.handlers import Filters, CommandHandler, MessageHandler
from celery.utils.log import get_task_logger
from celery import task
import requests

log = get_task_logger(__name__)
adapter = get_adapter()


def quote_movie(update, *args):
    response = requests.get('https://andruxnet-random-famous-quotes.p.mashape.com/?cat=movies', headers={
      "X-Mashape-Key": "BEjqsVLNGDmshmQ0ZxP0TC6j7wfDp1tlihvjsnUhhELDOJA7f5",
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

    adapter.add_handler(CommandHandler('quote', quote_movie, call_async=True))
