import random
from sys import exit

player = 10
boss = 10

moves = ['block', 'high attack', 'low attack']

while player > 0 and boss > 0:
    move_select = "Pick a move: block, high attack, or low attack\n>"

    p_attack = raw_input(move_select)
    b_attack = random.choice(moves)


    if p_attack != moves[0] and p_attack != moves[1] and p_attack != moves[2]:
        print"Nobody moves like that"
        print "Try again!"
    elif p_attack == b_attack:
        print "Mirrored! No Damage."
    elif p_attack == 'block' and b_attack == 'high attack':
        player = player - 3
        print "Player life: ", player
    elif p_attack == 'block' and b_attack == 'low attack':
        player = player - 1
        print "Player life: ", player
    elif p_attack == 'high attack' and b_attack == 'block':
        boss =  boss - 3
        print "Boss life :", boss
    elif p_attack == 'high attack' and b_attack == 'low attack':
        player = player - 3
        boss = boss - 5
        print "Player life :", player
        print "Boss life :", boss
    elif p_attack == 'low attack' and b_attack == 'block':
        boss = boss - 1
        print "Boss life :", boss
    elif p_attack == 'low_attack' and b_attack == 'high attack':
        player = player - 5
        boss = boss - 3
        print "Player life :", player
        print "Boss life :", boss
    else:
        print "Player life :", player
        print "Boss life :", boss
        exit(0)

print "Game Over"


