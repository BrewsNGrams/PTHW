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


def palm_tree_room():
    print "You enter a strange room full of exotic vegetation"
    print "A particularly ripe kiwi hangs just within your reach."
    print "Your starving and the fruit looks quite tempting."
    print "You also notice a coconut on the floor. You do enjoy"
    print "a good coconut but right off the tree they are rather difficult."
    print "to get open. Do you go for the kiwi or the coconut?"

    fruit_choice = raw_input('>')
    hungry = True

    while hungry == True:
        if fruit_choice == 'kiwi':
            print "At your first bite, the sweetness washes over your tongue."
            print "Then suddenly, the food turns to a wet, slimy mush."
            print "You look around the room and realize all the greenery"
            print "is gone, replaced by dead wood, swamp, and fungus all"
            print "around. You look in your hand and see that your kiwi"
            print "has turned to a rotting crab apple. You begin to feel"
            print "quite dizzy and light-headed. You realize this is the"
            print "end. Should've done the work for the coconut."
            print "Game OVer"
        elif fruit_choice == 'coconut':
            print "You decide to do the work for the coconut. Unfortunately"
            print "you have nothing on you to crack open the delicious"
            print "fruit. You look around the room for anything that might"
            print "be of any help. You notice a rather large hammer stuck"
            print "in the ground off to the right corner of the room."
            print "As you approach it, you notice a faint glow eminating"
            print "from it. Placing your hands around the handle, you"
            print "suddenly hear a voice inside your head. 'Only those"
            print "deemed worthy may carry the hammer of Thor! Tell me"
            print "young one, what makes you worthy of such a tremendous"
            print "weapon?' Racking your brain, you come up with three"
            print "possible responses\n1. You volunteer at homeless shelters"
            print "2. You own a yacht\n 3. COCONUT!"

            worthiness = raw_input('>')
            while heavy == True:
                if worthiness == '1':
                    print "'Liar!! You gave a homeless guy a half eaten"
                    print "sandwhich once and only because you didn't"
                    print "like the mayo. And neither did he!! No"
                    print "hammer for you!' The magic hammer transforms"
                    print "you into a turkey and swiss sandwhich with"
                    print "too much mayo.\n Game Over"
                    exit(0)
                elif worthiness == '2':
                    print "'Your a prideful and ignorant young man! You"
                    print "are not worthy of the great Hammer of Thor!!"
                    print "spend the rest of your days in shame below your"
                    print "precious yacht you love so much!' Suddenly, you"
                    print "find yourself underwater in scaly leggings and"
                    print "and an ugly orange long sleeve.... Your Aquaman"
                    print "... the fish guy. That sucks\n Game Over"
                    exit(0)
                elif worthiness == '3':
                    print "'Thor loved a good coconut too!! You"
                    print "Have been deemed worthy. Take the hammer"
                    print "the hammer and feast!' You manage to yank the"
                    print "hammer from the ground and smash that coconut"
                    print "real good. You lose a lot of the coconut water"
                    print "in the process but stil manage to save enough"
                    print "to satiate your thirst and the flesh of the thing"
                    print "seems to keep reappearing to satisfy your aching"
                    print "stomach. After your hearty meal you notice that"
                    print "a group of bushes have shifted revealing a tempur"
                    print "glass door. Peering through you see the most"
                    print "elaborate LAN setup you've seen in your life."
                    print "Do you check it out?"

                    door_check = raw_input('>')

                    if door_check == 'yes':
                        lan_room()
                    elif door_check == 'no':
                        print "you spend the rest of your days inside your"
                        print "single room paradise. Well played!"
                        exit(0)
                    else:
                        print "Does not compute"


def mansion_room():
    print "This is the mansion room."

def entrance_hall():
    opening = """
    Distracted thoughts veer you off-course on your way home.
    Upon looking up, your confronted with a rather odd looking house.
    It's a ranch style with very industrial looking decor.
    Metal side panels, a flat foof, and doors outlined by bolts
    Your not sure ehy but your drawn to the place.
    Before you know it your standing at the entrance.
    You open the door and a rather simple foyer with two doors.
    Not ordinary doors though. The left is surrounded by vibrant colors
    with a door that looks to be made from a palm tree.
    The right is lavished with reds and browns and looks like it
    belongs in a million dollar mansion. You've come this far so
    time to make a choice. The palm tree door on the left or the
    mansion door to the right?\n"""

    for i in opening:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.08)

    door_choice = raw_input('>')
    doors_closed = True

    while doors_closed == True:
        if door_choice == 'left':
            palm_tree_room()
            doors_closed = False
        elif door_choice == 'right':
            mansion_room()
            doors_closed = False
        else:
            print "Does not compute"


entrance_hall()
boss_fight(player_who)
