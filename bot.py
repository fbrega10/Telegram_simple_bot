from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from secret import getkey

updater = Updater(getkey(), use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello my friend! bot here...\ntype : /help to see available commands")

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available commands :-
    /youtube - to get the youtube url
    /maps - to get to google maps
    /gmail - open your gmail url
    /stack - to get to stackOverFlow
    /amaz - to get to amazon.com
    """)

def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your gmail link here => https://mail.google.com/"
    )
def maps_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Your google maps link here => https://maps.google.com/"
    )
def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Youtube link here => https://www.youtube.com/"
    )
def linkedin_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Linkedin link here => https://www.linkedin.com/"
    )
def stackoverflow_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "StackOverFlow link here => https://stackoverflow.com/"
    )
def amaz_url(update: Update, context: CallbackContext):
    update.message.reply_text(
        "amazon link here => https://www.amazon.com/"
    )
def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('maps', maps_url))
updater.dispatcher.add_handler(CommandHandler('amaz', amaz_url))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedin_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('stack', stackoverflow_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
