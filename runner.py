import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import API_TOKEN
from thats_you_defs import ThatsYouCommands

#################   ############# Init configs #########################################
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

############################# Handlers #########################################
if __name__ == '__main__':
    print('Running Bot...')

    updater = Updater(token=API_TOKEN, use_context=True)

    commands = ThatsYouCommands()

    updater.dispatcher.add_handler(CommandHandler('start', commands.start))
    updater.dispatcher.add_handler(CommandHandler('new', commands.new_game))
    updater.dispatcher.add_handler(CommandHandler('help', commands.show_help))
    updater.dispatcher.add_handler(MessageHandler(Filters.command, commands.unknown))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()
    print('Finish...')