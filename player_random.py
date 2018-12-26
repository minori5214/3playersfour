import random


class PlayerRandom:
    def __init__(self, turn, name='Random'):
        self.name = name
        self.myturn = turn

    def act(self, board):
        acts = board.get_possible_pos()
        i=random.randrange(len(acts))
        return acts[i]

    def getGameResult(self,board):
        pass