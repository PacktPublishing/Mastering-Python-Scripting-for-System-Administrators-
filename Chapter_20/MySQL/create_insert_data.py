import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')

with con_obj:
    
	cur_obj = con_obj.cursor()
	cur_obj.execute("DROP TABLE IF EXISTS books")

	cur_obj.execute("CREATE TABLE books(Id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(100))")

	cur_obj.execute("INSERT INTO books(Name) VALUES('Harry Potter')")
	cur_obj.execute("INSERT INTO books(Name) VALUES('Lord of the rings')")
	cur_obj.execute("INSERT INTO books(Name) VALUES('Murder on the Orient Express')")
	cur_obj.execute("INSERT INTO books(Name) VALUES('The adventures of Sherlock Holmes')")
	cur_obj.execute("INSERT INTO books(Name) VALUES('Death on the Nile')")

print("Table Created !!")
print("Data inserted Successfully !!")


