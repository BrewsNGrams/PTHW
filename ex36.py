from sys import exit
import random

print "Welcome to Adventure Game!"

player_who = raw_input('Please enter your name: ')

print "Good day", player_who, "and welcome to adventure game."

def boss_fight():
    player = 10
    boss = 15

    while player > 0 and boss > 0:
        print "The big boss appears. Time to take him down"

        move_select = "Pick a move: Block, Low Attack, High Attack\n>"
        moves = ['Block', 'Low Attack', 'High Attack']

        p_attack = raw_input(move_select)
        b_attack = random.choice(moves)

        if p_attack != moves[0] and p_attack != moves[1] and p_attack != moves[2]
