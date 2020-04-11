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
            self.scoreboard.update({player.name: {}})
            self.scoreboard[player.name].update({'points': 0})
        

    def show_scoreboard(self)-> str:
        """Apresenta o placar
        
        Returns:
            str -- Placar
        """
        scoreboard_msg: str = f"{'Placar':^25}\n" + '-'*35 + '\n'

        for name, values in self.scoreboard.items():
            scoreboard_msg += f"{name:^20}|{values['points']:>8}\n"

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
        return ''.join([f'{name} -> {vote}\n' for name, vote in self.votes.items()])


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
    

    def clear_votes(self) -> None:
        """Clear votes
        """
        self.votes = {}
    

    def update_score(self) -> None:
        """[summary]
        """
        for winner in self.round_winner():    
            self.scoreboard[winner]['points'] += POINTS_INCREMENT