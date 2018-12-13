import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
	cur_obj = con_obj.cursor()
	sql = """
		DELETE FROM books
		WHERE author = 'John Smith'
		"""
	cur_obj.execute(sql)
print("Data deleted successfully !!")

