
# Place your BotFather Token below
API_TOKEN = 'ADD_HERE'

# Path of the .txt file where the questions are stored
QUESTION_FILE = 'questions.txt'

##################################################  Constants  #################################################################
POINTS_INCREMENT = 100

# List of commands with a brief description
COMMANDS_en = {
    '/start': 'Start the Bot',
    '/new': 'Creates a new game',
    '/join': 'Log in to play the match',
    '/init': 'Starts a match',
    '/help': 'Displays the help screen with commands.',
    '/menu': 'Displays vote menu. Only in private chat.',
    '/vote': 'Assign a vote.',
}

############################################  Messages  ######################################################
from enum import Enum

class Messages_en(Enum):
    START = "Hello, welcome to the game that's you.\n\nTo create a new game use the /new command.\nIf you want to configure the game go to /config.\nAny questions access the command /help."

    NO_START_GROUP =  "To start the bot you must be in a group. Create a group and start the bot in a group using the /start command. You will only vote here"

    NO_START = "You need to use the /start command to start the group."

    NEW = "Hello! Let's start a new game, follow the instructions below.\n\n- Each person who wants to play must send the /join command to be added to the game.\n- When everyone sends their commands, the /init command must be sent to start the game.\nAny questions about the commands click on /help to see the list of available commands."

    UNKOWN = "Sorry, I didn't understand that command. \nClick on /help and look at the list of valid commands."

    HELP = "Hello, I'm here to help you.\n\nThe commands below are available for use:\n"

    QUESTION_FILE_ERR = "The question file was not found. Check the server."

    NO_ENOUGH_PLAYERS = "Not enough players to play, it takes 3 people for a game to start."

    NO_NEW_GAME = "You must start a new game first. Use the /new command."

    ALREADY_IN_GAME = "You're already in the game, take it easy."

    WAS_ADD = " was added to the game\."

    ASWER = "Answer the question:\n"

    PRIVATE_VOTE = 'Vote for the private chat by clicking @ThatsYouMths_bot. Submit /menu to display the voting options.'

    GAME_OVER = "The game is over\!"

    WINNER = " is the winner\!\!\! Congratulations for the victory\!"

    MENU_PRIVATE = "This command must be executed in the private chat. Click @ThatsYouMths_bot to vote."

    WHO_VOTE = "Who do you want to vote for?"

    NO_TIME_VOTE = "It is not time to vote. You must wait for a question."

    BACK_TO_GROUP = "Go back to the group and wait!"

    ALREADY_VOTE = " has already voted\!"

    YOU_ALREADY_VOTE = ", you have already voted! Go to the group and wait for the other people to vote."

    SHOW_VOTE = "Everyone has already voted\! The votes were\:\n"

    WINNERS_ROUND = "The winners of the round were:\n"

    INVALID_NAME = ", you entered an invalid name, vote again."
