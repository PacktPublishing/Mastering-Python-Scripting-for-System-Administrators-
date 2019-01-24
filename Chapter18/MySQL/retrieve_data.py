import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test')

with con_obj: 

	cur_obj = con_obj.cursor()
	cur_obj.execute("SELECT * FROM books")

	records = cur_obj.fetchall()

	for r in records:
		print(r)

