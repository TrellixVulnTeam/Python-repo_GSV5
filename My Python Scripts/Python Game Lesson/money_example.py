# convert xx.yy to xx dollars and yy cents
def convert(val):
	pound = int(val)
	pence = int(100 * (val - pound))
	return str(pound) + " pound and " + str(pence) + " pences"
    
# Tests
print convert(11.23)
print convert(11.20)
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)
