import MySQLdb 
con = MySQLdb.connect(user="root", passwd="Sai1993")
cur = con.cursor()
cur.execute('CREATE DATABASE taboola; ')