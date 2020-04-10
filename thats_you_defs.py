from settings import COMMANDS_en, Messages_en

class ThatsYouCommands():
    def __init__(self) -> None:
        pass
    

    def start(self, bot, update) -> None:
        """Initial message and verification if the bot is being started in a group.

        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        if bot.effective_chat.type == 'group':
            self.group_id: int = bot.effective_chat.id
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.start.value)
        else:
            update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.no_start.value)
            

    def new_game(self, bot, update) -> None:
        """After receiving the /new command starts a new game.
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        
        update.bot.send_message(chat_id=self.group_id, text=Messages_en.new.value)


    def show_help(self, bot, update) -> None:
        """Displays the help screen with commands.
        
        Arguments:
            bot {[type]} -- [description]
            update {[type]} -- [description]
        """
        head = Messages_en.help_msg.value + ''.join([f'{command} - {description}\n'for command, description in COMMANDS_en.items()])
        update.bot.send_message(chat_id=bot.effective_chat.id, text=head)


    def unknown(self, bot, update) -> None:
        """When a command is not recognized, the message below should be sent.
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.unkown.value)
