import random
from sys import exit

player = 10
boss = 15

moves = ['block', 'high attack', 'mid attack', 'low attack']

while player > 0 and boss > 0:
    move_select = "Pick a move: block, high attack, mid attack or low attack\n>"

    p_attack = raw_input(move_select)
    b_attack = random.choice(moves)

    if p_attack == b_attack:
        print "Boss did %s" % b_attack
        print "Mirrored! No Damage."
    elif p_attack == 'block' and b_attack == 'high attack':
        print "Boss did %s" % b_attack
        player = player - 4
        print "Player life: ", player
    elif p_attack == 'block' and b_attack == 'mid attack':
        print "Boss did %s" % b_attack
        player = player - 3
        print "Player life: ", player
    elif p_attack == 'block' and b_attack == 'low attack':
        print "Boss did %s" % b_attack
        player = player - 2
        print "Player life: ", player
    elif p_attack == 'high attack' and b_attack == 'block':
        print "Boss did %s" % b_attack
        boss =  boss - 4
        print "Boss life :", boss
    elif p_attack == 'high attack' and b_attack == 'mid attack':
        print "Boss did %s" % b_attack
        player = player - 4
        boss = boss - 5
        print "Player life :", player
        print "Boss life :", boss
    elif p_attack == 'high attack' and b_attack == 'low attack':
        print "Boss did %s" % b_attack
        player = player - 3
        boss = boss - 5
        print "Player life :", player
        print "Boss life :", boss
    elif p_attack == 'mid attack' and b_attack == 'block':
        print "Boss did %s" % b_attack
        boss = boss - 3
        print "Boss life :", boss
    elif p_attack == 'mid attack' and b_attack =='high attack':
        print "Boss did %s" % b_attack
        player = player - 5
        boss = boss - 4
        print "Player life :", player
        print "Boss life :", boss
    elif p_attack == 'mid attack' and b_attack == 'low attack':
        player = player - 3
        boss - boss - 4
        print "Player life :", player
        print "Boss life :", boss
    elif p_attack == 'low attack' and b_attack == 'block':
        print "Boss did %s" % b_attack
        boss = boss - 2
        print "Boss life: ", boss
    elif p_attack == 'low attack' and b_attack == 'high attack':
        print "Boss did %s" % b_attack
        player = player - 5
        boss = boss - 3
        print "Player life: ", player
        print "Boss life: ", boss
    elif p_attack == 'low attack' and b_attack == 'mid attack':
        player = player - 4
        boss = boss - 3
        print "Player life: ", player
        print "Boss life: ", boss
    else:
        print "Nobody moves like that!"
        print "Try again!"

if boss <= 0:
    print "You win!"
else:
    print "Game Over"


