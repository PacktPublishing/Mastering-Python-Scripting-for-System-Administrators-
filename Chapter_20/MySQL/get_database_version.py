import MySQLdb as mdb
import sys

con_obj = mdb.connect('localhost', 'test_user', 'test123', 'test');

cur_obj = con_obj.cursor()
cur_obj.execute("SELECT VERSION()")

version = cur_obj.fetchone()
   
print ("Database version : %s " % version)

con_obj.close()


