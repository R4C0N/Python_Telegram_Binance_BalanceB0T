import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from binance.client import Client
import keys

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def status(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('BINANCE BALANCE BOT ONLINE!'
        'type /margin = Displays MARGIN BALANCE')


def mbalance(update, context):
    client = Client(api_key=keys.SKey, api_secret=keys.PKey)
    M_btc = client.get_margin_account()
    f_MBTC = M_btc["totalNetAssetOfBtc"]
    float_BTC = float(f_MBTC)
    magin_BTC = 'MARGIN WALLET BITCOIN BALANCE:'
    update.message.reply_text(magin_BTC)
    update.message.reply_text(float_BTC)




def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    updater = Updater(keys.teltoken, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
   # dp.add_handler(CommandHandler("status", status))
    dp.add_handler(CommandHandler("margin", mbalance))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT
    updater.idle()


if __name__ == '__main__':
