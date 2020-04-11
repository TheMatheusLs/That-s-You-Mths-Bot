from settings import COMMANDS_en, Messages_en
from thats_you_game import ThatsYouGame

class ThatsYouCommands():
    def __init__(self) -> None:
        self.start_game_flag: bool = False
        self.new_game_flag: bool = False
    

    def start(self, bot, update) -> None:
        """Initial message and verification if the bot is being started in a group.

        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        if not self.check_group(bot, update):
            self.group_id: int = bot.effective_chat.id
            self.start_game_flag = True
            self.new_game_flag = False
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
        # Checks whether the command was executed in a group
        if self.check_group(bot, update):
            return None

        # Checks whether the Bot was started
        if not self.start_game_flag:
            update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.NO_START.value)
            return None

        self.new_game_flag = True

        try:
            self.Game = ThatsYouGame()
        except FileNotFoundError:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.QUESTION_FILE_ERR.value)
            return None

        update.bot.send_message(chat_id=self.group_id, text=Messages_en.NEW.value)


    def show_help(self, bot, update) -> None:
        """Displays the help screen with commands.
        
        Arguments:
            bot {[type]} -- [description]
            update {[type]} -- [description]
        """
        # Checks whether the command was executed in a group
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
        # Checks whether the command was executed in a group
        if self.check_group(bot, update):
            return None

        update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.UNKOWN.value)
    

    def init_game(self, bot, update) -> None:
        """Starts the match
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        # Checks whether the command was executed in a group
        if self.check_group(bot, update):
            return None

        # Checks whether the Bot was started
        if not self.start_game_flag:
            update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.NO_START.value)
            return None
            
        # Checks whether the game has started
        if not self.new_game_flag:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.NO_NEW_GAME.value)
            return None

        if not len(self.Game.players) > 0:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.NO_ENOUGH_PLAYERS.value)
            return None

        self.Game.create_scoreboard()

        update.bot.send_message(chat_id=self.group_id, text=self.Game.show_scoreboard())
        
        self.show_question(bot, update)



    def join_game(self, bot, update) -> None:
        """Add players to the game
        
        Arguments:
            bot {[type]} -- Update
            update {[type]} -- CallbackContext
        """
        # Checks whether the command was executed in a group
        if self.check_group(bot, update):
            return None

        # Checks whether the Bot was started
        if not self.start_game_flag:
            update.bot.send_message(chat_id=bot.effective_chat.id, text=Messages_en.NO_START.value)
            return None

        # Checks whether the game has started
        if not self.new_game_flag:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.NO_NEW_GAME.value)
            return None
        
        # Collect the user who sent the command
        user = bot.message.from_user
        user_name:str = user.name

        if user not in self.Game.players:
            update.bot.send_message(chat_id=self.group_id, text=user_name + Messages_en.WAS_ADD.value)
            self.Game.players.add(user)
            self.Game.players_name.append(user_name)
        else:
            update.bot.send_message(chat_id=bot.message.chat_id, text=Messages_en.ALREADY_IN_GAME.value, reply_to_message_id=True)

    def show_question(self, bot, update):

        if len(self.Game.questions) > 1:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.ASWER.value + self.Game.get_question())

            self.Game.vote_flag = True

            update.bot.send_message(chat_id=self.group_id, text=Messages_en.PRIVATE_VOTE.value)
        else:
            update.bot.send_message(chat_id=self.group_id, text=Messages_en.GAME_OVER.value)
            self.new_game_flag = False
            # Check Winner

            update.bot.send_message(chat_id=self.group_id, text='XXXX' + Messages_en.WINNER.value)