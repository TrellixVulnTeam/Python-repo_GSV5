from sys import argv
from Tkinter import Tk	# needed to copy key clipboard

script, key_select = argv

copier = Tk()	# create copier object from Tk class

copier.withdraw()
copier.clipboard_clear()	#clear the clipboard

testkey = "1105-3575-9930-4165\n6624-5776-5455-7862"
dellkey = '1082-3575-6284-3389'
utestLicence = '77542331214414562040'
serverkey = '55156709655667870788'

if ('1' in key_select):
	print testkey
	copier.clipboard_append(testkey)	#copy the string to clipboard
	
elif ('2' in key_select):
	print dellkey
	copier.clipboard_append(dellkey)	#copy the string to clipboard
	
elif ('3' in key_select):
	print utestLicence
	copier.clipboard_append(utestLicence)	#copy the string to clipboard

elif ('4' in key_select):
	print serverkey
	copier.clipboard_append(serverkey)		# copy the string to clipboard
	
else:
	print 'Parameter not recognised'
	pass

copier.destroy()
