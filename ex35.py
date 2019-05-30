# A simple text game with 4 rooms

# allows the program access to the function 'exit' which
# is found in the 'sys' package
from sys import exit

# creates a function called 'gold_room' which takes no parameters
def gold_room(): 
    """gold_room() asks the player to input how much gold they would like
    to take from the gold room. It checks the players input to enure that 
    its a number. If it's not, the player will get a 'dead' msg and the
    game will use the 'dead' function to end and exit the game. If it is 
    a number, it will check if that number is above or below 50. If above,
    the player will get a 'dead' msg and end and exit the game. If it is below
    50, the player will get a win msg then end and exit the game
    """

    print "This room is full of gold. How much do you take?"

    try:
        how_much = int(raw_input('>'))
        if how_much < 50:
            print "Your not greedy! You win!"
            exit(0)
        else:
            dead("You greedy bastard!")
    except ValueError:
        dead("That's not a number!")


# defines a function called 'bear_room' which takes no parameters
def bear_room():
    """bear_room lets the player know they are in a room with a honey eating
    bear that is blocking the next door. It then asks the player how they
    will move the bear. If they attempt to take the honey, bear_room()
    will output a 'dead' msg letting the player know they lost
    and end and exit the game. If they attempt to taunt the bear, the 
    bear will move and they will have the ability to open the door into 
    the gold room. The function will also give a 'dead' msg and end and 
    exit the game if the player tries to taunt the bear a 2nd time. If
    the player enters anything other than 'take honey' or 'taunt bear',
    the program will output an error msg and loop back to the beginning 
    where the player can try moving the bear again
    """

    print"There's a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    print "1. Take his honey"
    print "2. Taunt the bear"
    bear_moved = False

    while True:
        next = raw_input('>')

        if next == "1" or  "honey" in next:
            dead("The bear looks at you then slaps your face off.")
        elif (next == "2" or  "taunt" in next)  and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means.Try again"


def cthulu_room():
    """cthulu_room() lets the player know that they've entered
    a room with cthulu in it and that looking at cthulu makes
    them crazy. IT then offers 2 options, to flee or to eat their
    own head. If they flee, the player is brought back to the 
    beginning of the game (this simulates an endless loop where
    the player can never actually flee cthulu as many times as they
    try... appropriate). If they decide to eat their head the player
    will get a 'dead' msg and the 'dead' function will end and exit
    the game
    """
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input('>')

    if "flee" in next:
        start()
    elif "cross the streams":
        gozer()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()


# defines the function 'gozer()' which takes no parameters
def gozer():
    """gozer() warps the player to the top of the infamous
    55 Central Park West where the original ghostbusters 
    fought this functions namesake. There it asks the classic
    question "Are you a god" and promptly affords the player
    appropriate consequences for his/her choices. 
    """
    print "Suddenly you find yourself at the top of 55 Central Park West"
    print "A strange looking woman appears before you."
    print "She asks 'Are you a god?'"
    print "What do you say?"

    god_status = raw_input('>')
    if god_status == 'no':
        dead("She replies 'Then DIE!', which you promptly do so")
    elif god_status == 'yes':
        print "She replies 'Oh yea? Prove it!"
        proof = raw_input('>')
        if proof == 'thumb pull trick':
            print "Woah! You are a god! Let's rule the world!"
            print "You and Gozer spend many happy years together"
            print "enslaving and torturing mortals, having them"
            print "build temples in your name, and causing destruction"
            print "just for fun. You win!"
            
            exit(0)
        else:
            dead("You lie! Now DIE!!")
    else:
        line1 = "She cries 'That is meaningless!'"
        line2 = "A large marshmallow man eats you"
        line3 = "and you perish inside a belly of"
        line4 = "fluffy, sugary terror."

        dead("%s\n%s\n%s\n%s" % (line1, line2, line3, line4))
# defines a function called 'dead' which takes a single parameter
def dead(why):
    """ dead(why) will output a msg to the user as to the consequences
    of their action, congratulate him/her on his/her choice and end
    and exit the game
    """
    print why, "Good job!"
    exit(0)

# defines a function called 'start' which takes no paramerters
def start():
    """start(), as the name indicates, begins the game by telling the 
    user where they are and then giving the option of opening either 
    a door on the left or right. If the user tries to do anything other than
    open one of those two doors, they will get a 'dead' msg and the
    'dead' function will end and exit the game.
    """
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input('>')

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

# starts the game
start()
