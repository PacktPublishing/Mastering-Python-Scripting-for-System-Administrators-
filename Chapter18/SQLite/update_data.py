import sqlite3

con_obj = sqlite3.connect("test.db")
with con_obj:
	cur_obj = con_obj.cursor()
	sql = """
		UPDATE books 
		SET author = 'John Smith' 
		WHERE author = 'J.K Rowling'
		"""
	cur_obj.execute(sql)
print("Data updated Successfully !!")

