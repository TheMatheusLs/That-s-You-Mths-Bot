from collections import Counter
from settings import QUESTION_FILE
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