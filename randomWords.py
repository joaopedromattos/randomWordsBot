from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import logging
import os
import random


def start(update, context):
    context.bot.send_message(
                            chat_id=update.message.chat_id,
                            text=os.getenv("GREETINGS"))


def random_word(update, context):

    try:
        i = random.randint(0, len(randomWords) - 1)

        context.bot.send_message(
                            chat_id=update.message.chat_id,
                            text=randomWords[i])

    except(ValueError):  # This will execute case any issue occurs

        context.bot.send_message(
                            chat_id=update.message.chat_id,
                            text=os.getenv("WORD_NOT_FOUND"))
        print(os.getenv("WORD_NOT_FOUND"))


# I'll insert here the desired random words
randomWords = []

load_dotenv()  # Loading .env info...

logging.basicConfig(
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                level=logging.INFO)

# Instanciating an API to our bot...
updater = Updater(
                token=os.getenv("YOUR_TELEGRAM_BOT_API_TOKEN"),
                use_context=True
                )

dispatcher = updater.dispatcher

# Command handlers...
start_handler = CommandHandler('start', start)

random_word = CommandHandler('random_word', random_word)

# ...binding our command handlers.
dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_word)

updater.start_polling()  # Starts our bot server!
