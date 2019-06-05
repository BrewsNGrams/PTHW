from sys import exit
import random
import time
import sys

print "Welcome to Adventure Game!"

player_who = raw_input('Please enter your name: ')

print "Good day", player_who, "and welcome to adventure game."

def boss_fight(player_name):
    player = 10
    boss = 17

    while player > 0 and boss > 0:
        print "The big boss appears. Time to take him down"

        move_select = "Pick a move: block, low, mid, high\n>"
        moves = ['block', 'high', 'mid', 'low']

        p_attack = raw_input(move_select)
        b_attack = random.choice(moves)

        if p_attack == b_attack:
            print "Boss attacked with %s" % b_attack
            print "Mirrored! No Damage!."
        elif p_attack == 'block' and b_attack == 'high':
            print "Boss attacked with %s" % b_attack
            player = player - 4
            print "%s life: %d" % (player_name, player)
        elif p_attack == 'block' and b_attack == 'mid':
            print "Boss attacked with %s" % b_attack
            player = player - 3
            print "%s life: %d" % (player_name, player)
        elif p_attack == "block" and b_attack == "low":
            print "Boss attacked with %s" % b_attack
            player = player - 2
            print "%s life: %d" % (player_name, player)
        elif p_attack == "high" and b_attack == "block":
            print "Boss threw up a %s" % b_attack
            boss = boss - 4
            print "Boss life: %s" % boss
        elif p_attack == "high" and b_attack == "mid":
            print "Boss attacked with %s" % b_attack
            boss = boss - 5
            player = player - 4
            print "Boss life: %d" % boss
            print "%s life: %d" % (player_name, player)
        elif p_attack == "high" and b_attack == "low":
            print "Boss attacked with %s" % b_attack
            boss = boss - 5
            player = player - 3
            print "Boss life: %d" % boss
            print "%s life: %d" % (player_name, player)
        elif p_attack == "mid" and b_attack == "block":
            print "Boss threw up a %s" % b_attack
            boss = boss - 3
            print "Boss life: %d" % boss
        elif p_attack == "mid" and b_attack == "high":
            print "Boss attacked with %s" % b_attack
            boss = boss - 4
            player = player - 5
            print "Boss life: %d" % b_attack
            print "%s life: %d" % (player_name, player)
        elif p_attack == "mid" and b_attack == "low":
            print "Boss attacked with %s" % b_attack
            boss = boss - 4
            player = player - 3
            print "Boss life: %d" % b_attack
            print "%s life: %d" % (player_name, player)
        elif p_attack == "low" and b_attack == "block":
            print "Boss threw up a %s" % b_attack
            boss = boss - 2
            print "Boss life: %d" % boss
        elif p_attack == "low" and b_attack == "high":
            print "Boss attacked with %s" % b_attack
            player = player - 5
            boss = boss - 3
            print "Boss life: %d" % boss
            print "%s life: %d" % (player_name, player)
        elif p_attack == "low" and b_attack == "mid":
            print "Boss attacked with %s" % b_attack
            player = player - 4
            boss = boss - 3
            print "Boss life: %d" % boss
            print "%s life: %d" % (player_name, player)
        else:
            print "Nobody moves like that!"
            print "Try again!"


    if player > 0 and boss <= 0:
        print "You've defeated the big boss!"
        print "Congratulations!!"
        print "You Win!!!!"
    elif player <= 0 and boss <= 0:
        print "Tie goes to the boss"
        print "Game Over"
    else:
        print "Game Over"

boss_fight(player_who)
