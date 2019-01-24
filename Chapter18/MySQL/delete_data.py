import MySQLdb as mdb

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test');

cur_obj = con_obj.cursor()

cur_obj.execute("DELETE FROM books WHERE Id = 5");

try:
	con_obj.commit()
except:
	con_obj.rollback()


