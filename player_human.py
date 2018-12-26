from board import DRAW, EMPTY


class PlayerHuman:
    def __init__(self,turn):
        self.name="Human"
        self.myturn=turn

    def act(self,board):
        valid = False
        while not valid:
            try:
                act1, act2 = input("Where would you like to place " + str(self.name) + " (1-7) (1-7)? ").split()
                act1 = int(act1)
                act2 = int(act2)
                act = (act1 - 1)*7+act2-1
                if act >= 0 and act <= 48:
                    if board.board[act]!=EMPTY:
                        print ("The spot is not empty. Please try again.")
                    else:
                        valid=True
                        return act
                else:
                    print ("That is not a valid move! Please try again.")
            except Exception as e:
                    print ("LINE31 That is not a valid move! Please try again.")
                    print ("Input Example: 1 3")
        return act

    def getGameResult(self,board):
        if board.winner is not None and board.winner!=self.myturn and board.winner!=DRAW:
            print("I lost...")