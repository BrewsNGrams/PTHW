from sys import *
import sys
from playsound import playsound

def entrance_hall():
	print "You find yourself in a dark hallway"
	print "There is a faint light at the end of the hall"
	print "Approaching, you see two doors, to the left and right respectively"
	print "The left door looks like the entrance to a quaint little diner"
	print "The right door looks like a the front door to a NYC mansion."

	choice_made = False

	while choice_made == False:
		print "Which door will you chose?"
		door_choice = raw_input('>')
		if 'left' in door_choice:
			bobs_room()
			choice_made = True
		elif 'right' in door_choice:
			mansion_room()
			choice_made = True
		else:
			print "That's not an option"
			print "Try again"

def bobs_room():
	print "You open the door and find yourself in a quaint little burger joint"
	print "The proprietor of the establishment runs over to you and says,"
	print "'My name is Bob. This is my burger joint. So listen, my kids and wife"
	print "are driving me nuts!! I love them, I do but I need a break. Can you"
	print "cover me for an hour?' Will you help Bob?"
	choice_made = False

	while choice_made == False:
		cover_shift = raw_input('>')

		line1 = "Thank you so much!! Linda and Gene love music,"
		line2 = "Louise is a schemer, and Tina loves... well... butts"
		line3 =	"she loves butts... I don't know... do with that what"
		line4 =	"you can. Actually, don't. OH god, what am I gonna do with"
		line5 = "her... Anyway. Good luck. I'll be back in an hour.\n"

		thanks = "%s\n%s\n%s\n%s\n%s" % (line1, line2, line3, line4, line5)
		if cover_shift == 'yes':
			print thanks
			coverage()
			choice_made = True
		elif cover_shift =='no':
			print "'Please?'"
			beg = raw_input('>')
			if beg =='ok' or beg == 'fine':
				print thanks
				coverage()
				choice_made = True
			elif beg == 'no':
				print "Bob resigns to his fate and offers you a burger which"
				print "you graciously accept. Unfortunately, while trying to"
				print "cook your burger. Bob gets distracted by Linda and"
				print "the kids. The outside is cooked perfectly but the"
				print "inside not so much. As famished as you are, you devour"
				print "it, not noticing in the slightest how undercooked the"
				print "middle is. You head back home, oblivious to the virus"
				print "destroying you, slowly, inside. Three days later, you"
				print "die of mad cow disease."
				print "GAME OVER"
				choice_made = True
			else:
				print "Your not making any sense!!"
				print "Try again!"

def question_one():
	playsound("Windows Logon Sound.wav")

	choice_made = False
	print "Was that the Windows logon sound or logoff sound?!"
	while choice_made == False:
		guess_one = raw_input('>')

		if guess_one == 'logon':
			print "CORRRRECT!! ON TO THE NEXT QUESTION!!"
			choice_made = True
			question_two()
		elif guess_one == "logoff":
			print "Wrong again you imitation Gene Kelly!!"
			choice_made = True
		else:
			print "Watch that potty mouth of yours and try again!"

def question_two():
	print "What is the proper name for this classic Windows chime?!"
	print "You get 3 chances!!"

	playsound("TADA.WAV")

	choice_made = False
	chances = 3

	while choice_made == False and chances > 0:
		guess_two = raw_input('>')

		if guess_two == 'tada':
			print "You cheated!! No one knows that!! Next question!"
			choice_made = True
		else:
			print "Nope, try again!"
			chances = chances - 1
			print "You've got %d chances left!" % chances

	if guess_two == 'tada':
		question_three()
	else:
		print "WRONG!!! GAME OVER LOSER!!"


def question_three():
	print "Here would be question three"

def coverage():
	print "Bob introduces you to the family and heads on his way. The minute"
	print "he's gone, the kids ask you if you want to play a game., 'Sure'"
	print "you unwittingly reply. Gene excitedly grabs his keyboard. 'I am "
	print "going to make some AHMAZIING Windows sounds with my keyboard and you"
	print "will have to guess what they mean. READY?!!' You nod. 'Here comes"
	print "number one! (number 2 as well after that chili bowl.)'\n"

	question_one()


def mansion_room():
	print "You suddenly find yourself atop 55 Central Park West"
	print "In front of you is an elaborate alter of stone, guarded"
	print "by two large stone hounds. Standing in front of the alter"
	print "is a rather interesting character. What looks like a woman"
	print "scantily clad in pink and glittery tights and a pair of the"
	print "tallest heels you've ever seen. She looks directly into your"
	print "eyes and introduces herself. 'I am the great Gozer! In order"
	print "to move on, you must prove yourself worthy. Answer me this:"

	choice_made = False

	while choice_made == False:
		print "Are you a god?'"
		god_status = raw_input('>')
		if god_status == 'no':
			print "'The DIE!!!!'"
			print "Gozer manifests the Stay-Puff Marshmallow Man"
			print "He quickly snatches you up and swallows you whole"
			print "You die slowly, digesting in a belly of fluffy"
			print "sugary terror"
			print "GAME OVER"
			choice_made = True
		elif god_status == 'yes':
			prove_god()
			choice_made = True
		else:
			print "I wouldn't say that. She might get mad"
			print "Try again"

def prove_god():
	print "'Then prove it!!' Do you use your cosmic energies and indomitable"
	print "will to manifest a yet to exist lifeform or do that thing where it"
	print "looks like you can remove your thumb and then put it back on?"

	choice_made = False
	while choice_made == False:
		print "New lifeform or thumb trick?"
		proof= raw_input('>')

		if 'lifeform' in proof:
			print "You attempt to manipulate the very fabric of the universe to"
			print "align with your resolve. Unfortunately, your a dumb mortal"
			print "so you just end up looking like your trying to force a"
			print "rather uncomfortable bowel movement. Gozer grows impatient,"
			print "'Your proof now or pay the price!' You give it everything"
			print "you have and.... you let out a rather weak bit of gas. Gozer"
			print "chuckles. 'I knew it!! Now live the rest of your life in"
			print "agony deceiver!' With a a flick of his/her wrist you find"
			print "yourself in an office at Initech. You've been banished to a"
			print "life of programming and correcting TPS reports. OH GOD!!!!"
			print "GAME OVER"
			choice_made = True
		elif 'thumb' in proof:
			print "Gozer's eyes widen. 'That's amazing!!! How'd you do that?!!'"
			print "You shrug nervously '....magic?' Gozer, clearly impressed,"
			print "approves, 'You are clearly worthy. Your welcome to move on."
			print "Gozer and her alter slowly fade, revealing a studio door"
			print "surrounded by bright yellow bulbs. You've come this far."
			print "You carefully push open the door"
			meme_room()
			choice_made = True
		else:
			print "You can't do that. Try again."


def meme_room():
	print "You walk onto the stage of an ongoing game show"

entrance_hall()
