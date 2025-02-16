# Following the sqlite tutorial
# This file modifies the database file created in first.py

import sqlite3

# reconnect for subsequent session

conn = sqlite3.connect("C:\\Users\\terry.song\\Documents\\my python scripts\\database\\example.db")
cur = conn.cursor()

# use '?' as a place holder for SQL command, then provide values as 2nd arg
symbol = ('RHAT',)
cur.execute('SELECT * FROM stocks WHERE symbol=?', symbol)
print cur.fetchone()

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1001, 43.50),
		('2006-04-05', 'BUY', 'MSFT', 1000, 72.01),
		('2005-04-07', 'SELL', 'IBM', 500, 35.02),
		]

cur.executemany('INSERT INTO stocks VALUES (?, ?, ?, ?, ?)', purchases)

cur.execute('SELECT * FROM stocks ORDER BY price')
print cur.fetchall()

conn.commit()
conn.close()
