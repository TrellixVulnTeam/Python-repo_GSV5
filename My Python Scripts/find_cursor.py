from Mouse import Mouse
import time
import argparse

DEBUG = False

def ShowPos(mouse_obj, max_elapsed=None):
	"""
	A simple script that prints the updated mouse cursor coordinates out
	onto the console
	Parameter:  mouse_obj - a mouse object; max_elapsed - maximum
	duration for the script, will default 3600 seconds if not set
	"""
	start_time = time.time()	# time stamp at the start
	elapsed_time = time.time() - start_time		# elapsed time

	if not max_elapsed:
		max_elapsed = 3600

	# show current position
	pos = mouse_obj.get_position()
	print(pos)

	if DEBUG:
		print("Debug setting on")
		print("script duration: %d" % max_elapsed)

	while (elapsed_time < max_elapsed):
		if pos != mouse_obj.get_position():
			# update and show updated mouse position
			pos = mouse_obj.get_position()
			print(pos)
	print("Script finished")

if __name__ == "__main__":
	help_description = """Hello, how do you do?"""
	parser = argparse.ArgumentParser(description=help_description)
	help_argument = """Optional argument.  Who Dares Wins"""
	parser.add_argument('script_duration', nargs='?', default=None,\
			help=help_argument)
	args = parser.parse_args()

	cursor = Mouse()
	if args.script_duration:
		# argument exists, cast it as integer from string
		script_duration = int(args.script_duration)
		ShowPos(cursor, script_duration)
	else:
		ShowPos(cursor, args.script_duration)

