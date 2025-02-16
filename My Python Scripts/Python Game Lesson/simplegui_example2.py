# SimpleGUI programme example

# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
	global counter
	counter += 1
    
# Define event handler functions
def tick():		# timer event handler
	increment()
	print counter

def buttonpress():	# button event handler
	global counter
	counter = 0
    
# Create a frame, 100x100 square frame in this example
frame = simplegui.create_frame("SimpleGUI Test", 100, 100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", buttonpress)

# Start frame and timers
timer.start()
frame.start()
