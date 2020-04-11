from collections import Counter
from settings import QUESTION_FILE, POINTS_INCREMENT
import random

class ThatsYouGame():
    def __init__(self):
        self.scoreboard: dict = dict()
        self.players: set = set()
        self.players_name: list = list()
        self.questions: list = self.load_questions()
        self.question_number: int = 0
        self.votes: dict = dict()
        self.vote_flag: bool = False
    

    def load_questions(self) -> list:
        """Loads questions into a list
        
        Returns:
            list -- List of questions
        """
        try:
            with open(QUESTION_FILE, 'r', encoding='utf-8') as file:
                return [question.replace('\n', '') for question in file.readlines()]
        except:
            raise FileNotFoundError('The question file does not exist.')
    

    def create_scoreboard(self) -> None:
        """Starts the match score
        """
        for player in self.players:
            player_name = player.first_name + ' ' + player.last_name
            self.scoreboard.update({player_name: {}})
            self.scoreboard[player_name].update({'points': 0})
        

    def show_scoreboard(self)-> str:
        """Apresenta o placar
        
        Returns:
            str -- Placar
        """
        size_name = 14
        size_points = 6

        scoreboard_msg: str = f"`|{'SCOREBOARD':^{size_name + size_points + 1}}|`\n"
        scoreboard_msg += f"`|{'NAME':<{size_name}}|{'POINTS':>{size_points}}|`\n"

        for name, values in self.scoreboard.items():
            scoreboard_msg += f"*`|{name:<{size_name}}|{values['points']:>{size_points}}|`*\n"                    

        return scoreboard_msg
    

    def get_question(self) -> str:
        """Random question
        
        Returns:
            str -- Question
        """
        question = ''.join(random.sample(self.questions, 1))
        self.questions.remove(question)
        
        return question
    

    def check_vote(self, user, vote: str) -> bool:
        """Checks whether the vote is valid
        
        Arguments:
            user {[type]} -- Who voted?
            vote {str} -- Who was voted on?
        
        Returns:
            bool -- Valid vote?
        """
        if user in self.players and vote in self.players_name:
            return True
        return False
    

    def show_votes(self) -> str:
        """Show votes
        
        Returns:
            str -- Votes
        """
        return ''.join([f'{index}\. *{value[0]}* voted for *{value[1]}*\.\n' for index, value in enumerate(self.votes.items())])


    def show_winner_round(self) -> str:
        """Show winners
        
        Returns:
            str -- Winners
        """
        return '\n'.join(self.round_winner())
    

    def round_winner(self) -> list:
        """Checks the winner of the round
        
        Returns:
            list -- Winners
        """
        winner: list = list()

        for name, count in Counter(self.votes.values()).items():
            if count == max(Counter(self.votes.values()).values()):
                for key, value in self.votes.items():
                    if value == name:
                        winner.append(key)
        return winner
    

    def winner(self) -> list:

        winner: list = list()

        for name, points in self.scoreboard.items():
            if points['points'] == max([points['points'] for points in self.scoreboard.values()]):
                winner.append(name)
        return winner

    def clear_votes(self) -> None:
        """Clear votes
        """
        self.votes = {}
    

    def update_score(self) -> None:
        """[summary]
        """
        for winner in self.round_winner():    
            self.scoreboard[winner]['points'] += POINTS_INCREMENT