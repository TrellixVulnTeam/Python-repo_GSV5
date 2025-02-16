# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! - Andrea Crain

# This game is based on a common toy. It is a 
# round black ball with a clear plastic window. 
# The ball is filled with murky blue liquid
# and you use it as a fortune teller. You ask 
# a yes-or-no question and shake the ball. There 
# is a white many-sided die inside with answers, 
# and when you stop shaking, one of the sides
# floats up and is readable against the window.

# Here is a sample of the kind of
# output this program should produce:
#
# Your question was... Will I get rich?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably yes.
# 
# Your question was... Are the Cubs going to win the World Series?
# You shake the mystical octosphere.
# The cloudy liquid swirls, and a reply comes into view...
# The mystical octosphere says... Probably not.
#

# Let's get started!

# Up here, before everything else, import the random module
import random
# Type the command to import the random module above this line
# and make sure it is not indented at all.

# Next, fill in code for the function number_to_fortune
# This is a helper function.
# It should take in a number and send back a string
# 
# The possible numbers are between 0 through 7 inclusive
# (that means 0, 1, 2, 3, 4, 5, 6, or 7)
# and each number should translate to a fortune
# that would be the answer to a yes or no question.
#
# My suggested fortunes are:
# 0 - Yes, for sure!
# 1 - Probably yes.
# 2 - Seems like yes...
# 3 - Definitely not!
# 4 - Probably not.
# 5 - I really doubt it...
# 6 - Not sure, check back later!
# 7 - I really can't tell
#
# If somehow the function gets a number other than those 8
# it should send back a string saying that
# something was wrong with the input.

def number_to_fortune(number):
    # Fill in your code here.
    # Use an if...elif...else statement
    # to check each of the numbers between 0 and 7
    # and return the fortune as a string.
    
    if number == 0:
        return "Yes, for sure!"
    elif number == 1:
        return "Probably yes."
    elif number == 2:
        return "Seems like yes..."
    elif number == 3:
        return "Definitely not!"
    elif number == 4:
        return "Probably not."
    elif number == 5:
        return "I really doubt it..."
    elif number == 6:
        return "Not sure, check back later!"
    elif number == 7:
        return "I really can't tell."
    else:
        return "Something was wrong with my input."
    
    # Make sure all your code for the helper function is
    # indented by at least four spaces   
    
# TEST SECTION...    
# Uncomment this code to test if your number_to_fortune
# helper function is working. Highlight it all
# and hit control-shift-k to uncomment it all at once.
#print
#print number_to_fortune(0)
#print number_to_fortune(1)
#print number_to_fortune(2)
#print number_to_fortune(3)
#print number_to_fortune(4)
#print number_to_fortune(5)
#print number_to_fortune(6)
#print number_to_fortune(7)
#print number_to_fortune(19)
#print
# When you're done testing, comment it again.
# Highlight it all and hit control-k to comment it all at once
    
    
# Now fill in code for your main function.
# It must print the question out,
# Print a line saying you shake the octosphere
# Print out a line saying the liquid swirls and a reply comes into view
# And print what the fortune was
def mystical_octosphere(question):
    # Fill in your code below
    
    # Print a line including the original 
    # question to the console.    
    print "Your question was... " + question

    # Print the line "You shake the mystical octosphere."    
    print "You shake the mystical octosphere."
    
    # Use randrange to put a random number between 0 and 7 
    # into a variable called answer_number
    answer_number = random.randrange(0, 8)
    
    # Use the helper function to translate
    # the number you just randomly selected
    # into a fortune, and store it in a
    # variable called answer_fortune
    answer_fortune = number_to_fortune(answer_number)

    # Build suspense by printing a line that says
    # The cloudy liquid swirls, and a reply comes into view...
    print "The cloudy liquid swirls, and a reply comes into view..."
    
    # Print a line that says 
    # The mystical octosphere says...
    # and the fortune you put into answer_fortune
    print "The mystical octosphere says... " + answer_fortune    

    # Print a blank line
    print
    
    
    # Make sure all your code for the main function
    # is indented by at least four spaces
    # ("At least" means it can be more than four but not less.)    

# These lines runs your main function!
# You can change the questions if you wish.
# Only yes-or-no style questions will make sense.
mystical_octosphere("Will I get rich?")
mystical_octosphere("Are the Cubs going to win the World Series?")