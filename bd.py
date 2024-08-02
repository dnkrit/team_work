import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

conn.commit()

cur.execute('SELECT * FROM example')
rows = cur.fetchall()
print(rows)
