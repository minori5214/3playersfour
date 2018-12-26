import pickle

from datetime import datetime

from player_alpha_random import PlayerAlphaRandom
from player_human import PlayerHuman
from player_ql import PlayerQL
from player_dqn import PlayerDQN
from player_dqn_conv import PlayerDQN_CONV
from player_random import PlayerRandom
from board import PLAYER_X, PLAYER_O, PLAYER_I
from game_organizer import GameOrganizer

def repeat_dumped_vs_dumped_vs_dumped(repeat=49):
    file1 = 'dump/dqn_vs_ar_ar_p1.pkl'
    file2 = 'dump/dqn_vs_ar_ar_p2.pkl'
    file3 = 'dump/dqn_vs_ar_ar_p3.pkl'
    for i in range(repeat):
        print("%dth train" % i)
        with open(file1, mode='rb') as f:
            p1 = pickle.load(f)
            p1.myturn = PLAYER_X
            p1.name = "DQ1"
        with open(file2, mode='rb') as f:
            p2 = pickle.load(f)
            p2.myturn = PLAYER_O
            p2.name = "DQ2"
        with open(file3, mode='rb') as f:
            p3 = pickle.load(f)
            p3.myturn = PLAYER_I
            p3.name = "DQ3"
        game = GameOrganizer(p1, p2, p3, 2000, False, False, 100)
        game.progress()

        file1 = 'dump/dqn_vs_ar_ar_p1.pkl'
        file2 = 'dump/dqn_vs_ar_ar_p2.pkl'
        file3 = 'dump/dqn_vs_ar_ar_p3.pkl'
        with open(file1, mode='wb') as f:
            pickle.dump(p1, f)
        with open(file2, mode='wb') as f:
            pickle.dump(p2, f)
        with open(file3, mode='wb') as f:
            pickle.dump(p3, f)
    print("COMPLETE")

def dqn_conv_vs_random_vs_random(num):
    p1 = PlayerDQN_CONV(PLAYER_X, 'DQ1')
    p2 = PlayerRandom(PLAYER_I, 'Random1')
    p3 = PlayerRandom(PLAYER_O, 'Random2')
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

    with open('dump/dqn_conv_vs_ql_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)

def random_vs_random_vs_random(num):
    p1 = PlayerRandom(PLAYER_X, 'Random1')
    p2 = PlayerRandom(PLAYER_O, 'Random2')
    p3 = PlayerRandom(PLAYER_I, 'Random3')
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

def human_vs_random_vs_random(num):
    p1 = PlayerHuman(PLAYER_X)
    p2 = PlayerRandom(PLAYER_O, 'Random1')
    p3 = PlayerRandom(PLAYER_I, 'Random2')
    game = GameOrganizer(p1, p2, p3)
    game.progress()

def dqn_vs_random_vs_random(num):
    p1 = PlayerDQN(PLAYER_X, 'DQ1')
    p2 = PlayerRandom(PLAYER_I, 'Random1')
    p3 = PlayerRandom(PLAYER_O, 'Random2')
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

    with open('dump/dqn_vs_rm_rm_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)

def dqn_conv_vs_alpha_random_vs_alpha_random(num):
    p1 = PlayerDQN_CONV(PLAYER_X, 'DQ1')
    p2 = PlayerAlphaRandom(PLAYER_O)
    p3 = PlayerAlphaRandom(PLAYER_O)
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

    with open('dump/dqn_conv_vs_ar_ar_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)

def human_vs_dumped_vs_dumped():
    p1 = PlayerHuman(PLAYER_X)
    with open('dump/dqn_vs_ar_ar_p1.pkl', mode='rb') as f:
        p2 = pickle.load(f)
        p2.myturn = PLAYER_O
    with open('dump/dqn_vs_ar_ar_p2.pkl', mode='rb') as f:
        p3 = pickle.load(f)
        p3.myturn = PLAYER_I
    p2.e = 0
    p3.e = 0
    game = GameOrganizer(p1, p2, p3)
    game.progress()

def human_vs_human_vs_human():
    p1 = PlayerHuman(PLAYER_X)
    p2 = PlayerHuman(PLAYER_I)
    p3 = PlayerHuman(PLAYER_O)
    game = GameOrganizer(p1, p2, p3)
    game.progress()

def alpha_random_vs_dumped_vs_dumped():
    p1 = PlayerAlphaRandom(PLAYER_X)
    with open('dump/dqn_conv_vs_ql_2018_12_25_07_23_30.pkl', mode='rb') as f:
        p2 = pickle.load(f)
        p2.myturn = PLAYER_O
    with open('dump/dqn_conv_vs_ql_2018_12_25_07_23_30.pkl', mode='rb') as f:
        p3 = pickle.load(f)
        p3.myturn = PLAYER_I
    p2.e = 0
    p3.e = 0
    game = GameOrganizer(p1, p2, p3, 3000, False, False, 100)
    game.progress()

    with open('dump/dqn_vs_ar_ar_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p2, f)

def dumped_vs_dumped_vs_dumped(num):
    with open('dump/dqn_conv_vs_ar_ar_2018_12_25_08_29_39.pkl', mode='rb') as f:
        p1 = pickle.load(f)
        p1.myturn = PLAYER_X
        p1.name = "DQ1"
    with open('dump/dqn_conv_vs_ar_ar_2018_12_25_08_29_39.pkl', mode='rb') as f:
        p2 = pickle.load(f)
        p2.myturn = PLAYER_O
        p2.name = "DQ2"
    with open('dump/dqn_conv_vs_ar_ar_2018_12_25_08_29_39.pkl', mode='rb') as f:
        p3 = pickle.load(f)
        p3.myturn = PLAYER_I
        p3.name = "DQ3"
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

    with open('dump/dqn_vs_ar_ar_p1_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)
    with open('dump/dqn_vs_ar_ar_p2_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p2, f)
    with open('dump/dqn_vs_ar_ar_p3_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p3, f)

def ql_vs_ql_vs_ql(num):
    p1 = PlayerQL(PLAYER_X, 'Q1')
    p2 = PlayerQL(PLAYER_I, 'Q2')
    p3 = PlayerQL(PLAYER_O, 'Q3')
    game = GameOrganizer(p1, p2, p3, num, False, False, 100)
    game.progress()

    with open('dump/ql_vs_ql_ql_%s.pkl' % sdate(), mode='wb') as f:
        pickle.dump(p1, f)

def sdate():
    return datetime.now().strftime('%Y_%m_%d_%H_%M_%S')