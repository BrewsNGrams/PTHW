print "How old are you?",
age = int(raw_input())
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "Where are you from?",
home = raw_input()
print """
What's your favorite pizza style:
Brooklyn, Chicago, or West Coast?
""",
pizza_style = raw_input()


print "So you're %d old, %s tall, and %s heavy." % (age, height, weight)
print "And your from %s." % home
print "And you like %s pizza" % pizza_style

if pizza_style == "Brooklyn":
    print "Yea, NYC pizza's the best!!"
elif pizza_style == "Chicago":
    print "Deep dish ain't bad. NY's is better though"
elif pizza_style == "West Coast":
    print "Veggies ARE good for you (even with all that cheese)."
else:
    print "Does not compute"
