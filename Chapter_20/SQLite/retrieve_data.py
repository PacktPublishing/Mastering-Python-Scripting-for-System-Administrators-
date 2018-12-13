import sqlite3

con_obj = sqlite3.connect('test.db')

cur_obj = con_obj.execute("SELECT title, author from books")
for row in cur_obj:
	print ("Title = ", row[0])
	print ("Author = ", row[1], "\n")

con_obj.close()

