"""
This is weekly mini-project number II
The programme recreates the Rock-Paper-Scissors-Lizard-Spock
Creator: Song, Jiawen (Terry)

The key idea of this programme is to equate the strings 'rock', 'paper',
'scissors', 'lizard', 'Spock' to numbers as followed

0 - rock
1 - Spock
2 - paper
3 - lizard
4 - scissors

The rules of the game is as followed

Scissors cut Paper
Paper covers Rock
Rock crushes Lizard
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitate Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporises Rock
Rock crushes Scissors
"""

import random	# the programme needs random number as opposing response

# helper functions

def name_to_number(name):
	# covert name to number using dictionary type
	# The function returns an integer

	conversion = {'rock':0, 'Spock':1, 'paper':2, 'lizard':3, 'scissors':4}

	# possible choices
	selection = ['rock', 'Spock', 'paper', 'lizard', 'scissors']

	if name in selection:	# check if name is valid
		converted = conversion.get(name) # get corresponding number
		return converted
	else:		# invalid name
		print 'The choice is invalid'
	# end of if-else
# end of definition

def number_to_name(number):
	# convert number to name using dictionary type
	# The functions returns a string

	conversion = {0:'rock', 1:'Spock', 2:'paper', 3:'lizard', 4:'scissors'}

	if (number >= 0) and (number < 5):	# check number is in range
		converted = conversion.get(number) # get corresponding name
		return converted
	else:		# invalid number
		print 'The number is out of range'
	# end of if-else
# end of definition

def give_reason(first, second):
	"""
	The function gives the reason of the outcome using dictionary
	The two parameters are integers, first is the winner choice,
	second is the loser choice.  The order cannot be altered
	The function returns a string
	"""

	# rock paper siccors lizard Spock rules
	the_rule = {(4, 2):"Scissors cut paper",
			(2, 0):"Paper covers rock",
			(0, 3):"Rock crushes lizard",
			(3, 1):"Lizard poisons Spock",
			(1, 4):"Spock smashes scissors",
			(4, 3):"Scissors decapitate lizard",
			(3, 2):"Lizard eats paper",
			(2, 1):"Paper disproves Spock",
			(1, 0):"Spock vaporises rock",
			(0, 4):"Rock crushes scissors"}

	# check whether the two parameter values are in range
	firstInRange = (first >= 0) and (first < 5)	# boolean variable
	secondInRange = (second >=0) and (second < 5)	# boolean variable

	if firstInRange and secondInRange:
		return the_rule[(first, second)]
	else:
		print "Parameter values not in range"
	# end of if-else
# end of definition

# main function

def rpsls(player_choice):
	"""
	This is the main function of the programme
	This function generates choice of weapon and compares against that
	of the player, then determines of the game and prints the outcome
	"""
	print "\n"	# print a blank link
	print "Player chooses " + player_choice	# print player choice

	player = name_to_number(player_choice)	# convert player choice

	computer = random.randrange(0, 5)	# random computer choice
	computer_choice = number_to_name(computer)

	print "Computer chooses " + computer_choice # print comp choice

	difference = player - computer		# calculate the difference

	if not(difference == 0):	# the choices are different
		if (difference % 5) < 3:# comp chooses anticlockwise
			print give_reason(player, computer)
			print "Player wins!"
		
		else:			# comp chooses clockwise
			print give_reason(computer, player)
			print "Computer wins!"
		# end of if-else
	
	else:		# the choices are the same
		print "Player and computer tie"
	# end of if-else
# end of definition

rpsls('rock')
rpsls('Spock')
rpsls('paper')
rpsls('lizard')
rpsls('scissors')

