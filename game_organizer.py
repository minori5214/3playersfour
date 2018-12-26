import random

from board import DRAW, Board


class GameOrganizer:

    act_turn=0
    winner=None

    def __init__(self, px, po, pi, nplay=1, showBoard=True, showResult=True, stat=100):
        self.player_x=px
        self.player_o=po
        self.player_i=pi
        self.nwon={px.myturn:0,po.myturn:0,pi.myturn:0,DRAW:0}
        self.nplay=nplay
        self.players=(self.player_x,self.player_o,self.player_i)
        self.board=None
        self.disp=showBoard
        self.showResult=showResult
        self.player_turn=self.players[random.randrange(3)]
        self.nplayed=0
        self.stat=stat

    def progress(self):
        while self.nplayed < self.nplay:
            self.board = Board()
            turn = 0

            while self.board.winner == None:
                turn += 1
                if self.disp:
                    print("Turn: ", turn)
                    print("Turn is " + self.player_turn.name)

                act = self.player_turn.act(self.board)
                self.board.move(act,self.player_turn.myturn)

                if self.disp:
                    self.board.print_board()

                if self.board.winner != None:
                    # notice every player that game ends
                    for i in self.players:
                        i.getGameResult(self.board)

                    if self.board.winner == DRAW:
                        if self.showResult:print ("Draw Game")
                    elif self.board.winner == self.player_turn.myturn:
                        out = "Winner : " + self.player_turn.name
                        if self.showResult: print(out)
                    else:
                        print ("Invalid Move!")
                    self.nwon[self.board.winner]+=1
                else:
                    self.switch_player()
                    # Notice other player that the game is going
                    self.player_turn.getGameResult(self.board)

            self.nplayed += 1
            if self.nplayed%self.stat==0 or self.nplayed==self.nplay:
                print(self.player_x.name+":"+str(self.nwon[self.player_x.myturn])+","
                        +self.player_o.name+":"+str(self.nwon[self.player_o.myturn])+","
                        +self.player_i.name+":"+str(self.nwon[self.player_i.myturn])
                        +",DRAW:"+str(self.nwon[DRAW]))


    def switch_player(self):
        if self.player_turn == self.player_x:
            self.player_turn=self.player_o
        elif self.player_turn == self.player_o:
            self.player_turn=self.player_i
        else:
            self.player_turn=self.player_x