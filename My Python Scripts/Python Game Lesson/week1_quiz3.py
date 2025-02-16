"""
This script is for question 7 of week 1 quiz
"""
import math

def polygonArea(sideNum, sideLen):
	"""
	Calculates the area of a polygon
	sideNum - number of polygon sides
	sideLen - length of each side
	"""
	sideNum = float(sideNum)
	sideLen = float(sideLen)

	area = 0.25 * sideNum * (sideLen**2) / math.tan(math.pi/sideNum)
	return area
# end of the function definition

print polygonArea(5, 7)
print polygonArea(7, 3)

