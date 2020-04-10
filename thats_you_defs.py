from settings import COMMANDS_en, Messages_en

class ThatsYouCommands():
    def __init__(self) -> None:
        self.start_game_flag: bool = False
    

    def start(self, bot, update) -> None:
        """Initial message and verification if the bot is being started in a group.

        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        if not self.check_group(bot, update):
            self.group_id: int = bot.effective_chat.id
            self.start_game_flag = True
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.START.value)


    def check_group(self, bot, update) -> bool:  
        """Checks whether the command was executed in a group.
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        
        Returns:
            bool -- Returns true if the command is done in a group
        """
        if bot.effective_chat.type != 'group':
            update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.NO_START_GROUP.value)
            return True
        return False


    def new_game(self, bot, update) -> None:
        """After receiving the /new command starts a new game.
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        if self.check_group(bot, update):
            return None

        if not self.start_game_flag:
            update.bot.send_message(chat_id=bot.effective_chat.id, text='nedd start first')
            return None

        update.bot.send_message(chat_id=self.group_id, text=Messages_en.NEW.value)


    def show_help(self, bot, update) -> None:
        """Displays the help screen with commands.
        
        Arguments:
            bot {[type]} -- [description]
            update {[type]} -- [description]
        """
        if self.check_group(bot, update):
            return None

        head = Messages_en.HELP.value + ''.join([f'{command} - {description}\n'for command, description in COMMANDS_en.items()])
        update.bot.send_message(chat_id=bot.effective_chat.id, text=head)


    def unknown(self, bot, update) -> None:
        """When a command is not recognized, the message below should be sent.
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        if self.check_group(bot, update):
            return None

        update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.UNKOWN.value)