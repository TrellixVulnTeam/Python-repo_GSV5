import sqlite3

# Create or open a file with a Sqlite3 database
db = sqlite3.connect('..\database\mybase.db')

# Get a cursor object
cursor = db.cursor()

# Create an user table with name, phone, email and password
cursor.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
		phone TEXT, email TEXT unique, password TEXT)''')

# Save the changes
db.commit()

# to drop a table
cursor.execute('''CREATE TABLE useless(id DOUBLE PRIMARY KEY, name TEXT,
		phone TEXT, email TEXT unique)''')

cursor.execute('''DROP TABLE useless''')
db.commit()

# Insert data in the database
name1 = 'Jenson Button'
phone1 = '12345678'
email1 = 'jbutton@mclaren.com'
password1 = 'abcdefg'

name2 = 'Lewis Hamilton'
phone2 = '23456781'
email2 = 'lhamilton@mercagm.com'
password2 = 'bcdefgl'

# use ? as place holder
cursor.execute('''INSERT INTO users(name, phone, email, password)
		VALUES(?, ?, ?, ?)''', (name1, phone1, email1, password1))
print 'user1 insert'

# pass a dictionary using the ":keyname" place holder
cursor.execute('''INSERT INTO users(name, phone, email, password)
		VALUES(:name, :phone, :email, :password)''',
		{'name':name2, 'phone':phone2, 'email':email2,
		'password':password2})
print 'user2 insert'

db.commit()
db.close()
