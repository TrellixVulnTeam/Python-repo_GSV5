import sqlite3

database = '..\database\mybase.db'
db = sqlite3.connect(database)
cursor = db.cursor()

# more data for user table
name1 = 'Nico Rosberg'
phone1 = '3456789'
email1 = 'nrosberg@mercamg.com'
password1 = '23gde325'

name2 = 'Felipe Massa'
phone2 = '8901234'
email2 = 'fmassa@ferrari.com'
password2 = '983uie313'

name3 = 'Adrian Sutil'
phone3 = '3859273'
email3 = 'asutil@sauber.com'
password3 = 'k3j2do98'

# Insert multiple users at once
users = [(name1, phone1, email1, password1),
	(name2, phone2, email2, password2),
	(name3, phone3, email3, password3)]

# use executemany function
cursor.executemany('''INSERT INTO users(name, phone, email, password)
		VALUES(?, ?, ?, ?)''', users)
db.commit()
db.close()
