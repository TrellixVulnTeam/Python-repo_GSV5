import re, urllib

try:
	import urllib2
except:
	pass

sites = 'google yahoo bbc msn'.split()

# compile a pattern to make code more efficient
pat = re.compile(r'<title>+.*</title>+', re.I|re.M)

for s in sites:
	print('Search: ' + s)

	try:
		u = urllib.urlopen('https://www.' + s + '.com')
	except:
		u = urllib2.urlopen('https://' + s + '.com')
	
	text = u.read()
	title = re.findall(pat, str(text))

	print(title[0])

