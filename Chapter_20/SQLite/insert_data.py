import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
	cur_obj = con_obj.cursor()

	cur_obj.execute("INSERT INTO books VALUES ('Pride and Prejudice', 'Jane Austen')")
	cur_obj.execute("INSERT INTO books VALUES ('Harry Potter', 'J.K Rowling')")
	cur_obj.execute("INSERT INTO books VALUES ('The Lord of the Rings', 'J. R. R. Tolkien')")
	cur_obj.execute("INSERT INTO books VALUES ('Murder on the Orient Express', 'Agatha Christie')")
	cur_obj.execute("INSERT INTO books VALUES ('A Study in Scarlet', 'Arthur Conan Doyle')")
	con_obj.commit()

print("Data inserted Successfully !!")
