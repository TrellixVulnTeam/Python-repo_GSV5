import re as regex
from sys import argv

script, subject = argv

pattern = regex.compile('[a-z]+')	# pattern to be matched

result = pattern.match(subject)
print result

