from sys import exit

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
        dead("She replies 'Then DIE!', which you do so promptly.")
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

gozer()
