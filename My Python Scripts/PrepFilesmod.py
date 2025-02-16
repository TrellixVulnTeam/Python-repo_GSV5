import os
import sys
import xml.etree.ElementTree as ET

def _ParamVerifier_(fileLocation, OnOff):
# The function is used internally by other module functions to verify whether the parameters are valid.  The function is to provide error handling ability
# fileLocation is a string containing the directory of the Invincea GA build

	OnOff = str(OnOff)	#in case OnOff is not a string
	validNum = OnOff.isdigit()
	validPath = os.path.exists(fileLocation)
	
	if validNum and validPath:
		return True
	else:
		if not (validNum):
			print 'The parameter OnOff must be a number of either 0 or 1'
		
		if not (validPath):
			print 'The file path is not valid'
		
		return False

def UserModifiableOnOff(fileLocation, OnOff):
# The function is specificly for enabling and disabling all the functions with user modifiable option.  The two parameters: fileLocation, OnOff
# fileLocation is a string containing the directory of the preferences.xml
# OnOff is a string containt a number.
# If OnOff == 1, all user modifiable option will be enabled
# If OnOff == 0, all user modifiable option will be disabled

	if _ParamVerifier_(fileLocation, OnOff):
		theFile = fileLocation + '\\preferences.xml'
		On_Off = int(OnOff)
	
		#read the xml file from the location defined by parameter
		fileTree = ET.parse(theFile)
		fileRoot = fileTree.getroot()
	
		keyAttrib = 'user_modifiable'	#key attribute
		searchKey = './/*[@' + keyAttrib + ']'	#search key by XPath support
	
		if On_Off > 0:
			newValue = 'true'
		else:
			newValue = 'false'
		
		#search by attribute thanks to XPath support in ElementTree 1.3
		for elem in fileRoot.iterfind(searchKey):
			elem.set(keyAttrib, newValue)
		
		fileTree.write(theFile)
		
	else:
		pass

def keyChanger(fileLocation, keyType):
# The function is specificly for changing the licence key in the installer packet.  The two parameters: fileLocation, keyType
# fileLocation is a string containing the file location
# keyType is a string containing a number
# if keyType == 1, an enterprise test licence key will be used
# if keyType == 2, a dell protective workspace key will be used, but not recommended
# if keyType == 3, an utest licence key will be used
# if keyType == 4, an incomplete enterprise test licence key

	#Invincea Enterprise test key
	testkey = "1105-3575-9930-4165\n6624-5776-5455-7862"
	badtestkey = "6624-5776-5455-7862"
	
	#dell protective workspace licence key
	dellkey = '1082-3575-6284-3389'
	
	#utest licence key
	utestLicence = '77542331214414562040'
	
	if _ParamVerifier_(fileLocation, keyType):
		
		keyToUse = int(keyType)
		
		theFile = fileLocation + '\\activationkey.txt'
		target = open(theFile, 'w')
		target.truncate()
		
		if keyToUse == 1:
			target.write(testkey)
			
		elif keyToUse == 2:
			target.write(dellkey)
			
		elif keyToUse == 3:
			target.write(utestLicence)
			
		elif keyToUse == 4:
			target.write(badtestkey)
		
		else:
			print 'Parameter not recognised'
			pass
		
		target.close()
	
	else:
		pass

def FunctionOnOff(fileLocation, functionTag, OnOff):
# The function is for enabling or disabling any function specified in the preferences.xml.  The two parameters: fileLocation, functionTag, OnOff
# fileLocation is a string containing the directory of the preferences.xml
# functionTag is a string containing the function which to be enabled or disabled
# OnOff is a string containt a number.
# If OnOff == 1, all user modifiable option will be enabled
# If OnOff == 0, all user modifiable option will be disabled

	if _ParamVerifier_(fileLocation, OnOff):
		theFile = fileLocation + '\\preferences.xml'
		On_Off = int(OnOff)
		
		if On_Off > 0:
			newValue = 'true'
		else:
			newValue = 'false'
		
		#read the xml file from the location defined by parameter
		fileTree = ET.parse(theFile)
		fileRoot = fileTree.getroot()
		
		#a function only appears once in the preferences.xml, no recurssive loop is needed
		for tag in fileRoot.iter(functionTag):
			tag.set('enabled', newValue)
				
		fileTree.write(theFile)
	
	else:
		pass

def AddNewFunction(fileLocation, functionTag, OnOff):

	OnOff = str(OnOff)	#in case OnOff is not a string
	
	# error handling when user sends a bad parameter
	if not (OnOff.isdigit()):
		print 'The parameter OnOff must be a number of either 0 or 1'
		exit(0)
	
	theFile = fileLocation + '\\preferences.xml'
	On_Off = int(OnOff)
	
	if On_Off > 0:
		newValue = 'true'
	else:
		newValue = 'false'
	
	# read the xml file from the location defined by parameter
	fileTree = ET.parse(theFile)
	fileRoot = fileTree.getroot()
	
	change = True		#flag to modify the xml file
	
	# read through the xml file to make sure the new tag is not in the file
	for element in fileRoot:
		tag = ET.tostring(element)	#cast the element in the preferences file to string
		if functionTag in tag:
			print '%s has already been added to the file' % functionTag
			change = False	#set flag not to modify the file
			break
		else:
			pass
	
	if change:
		newNode = ET.Element(functionTag)
		fileRoot.insert(len(fileRoot), newNode)		#add the new element to the xml file as the last element
	
		fileTree.write(theFile)
		
		FunctionOnOff(fileLocation, functionTag, On_Off)	#enable or disable it

def FunctionModify(fileLocation, functionTag, attribute, newValue):
# functionTag is a string containing the function
# attribute is a string containing the attribute in t
	theFile = fileLocation + '\\preferences.xml'
	
	#read the xml file from the location defined by parameter
	fileTree = ET.parse(theFile)
	fileRoot = fileTree.getroot()
	
	searchKey = './/*[@' + attribute + ']'	#search key by XPath support
	
	#a function only appears once in the preferences.xml, no recurssive loop is needed
	for tag in fileRoot.iter(functionTag):
		tag.set(attribute, newValue)
	
	fileTree.write(theFile)
	
