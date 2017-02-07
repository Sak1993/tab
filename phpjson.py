import json
#import mysql.connector
import pymysql

testFile = open("/Users/sgottam/Documents/taboola/cpxi_lockerroom.json")
data = json.load(testFile)

mydb = pymysql.connect(host='localhost',user='root',password='Sai',db='taboola',charset='utf8',port=3306)

cursor =mydb.cursor()

list1 = data["results"]

cursor.executemany("""INSERT INTO cpxi_lockerroom_site_breakdown(date,site,site_name,campaign,clicks,impressions,spent,ctr,cpm,cpc,cpa,cpa_actions_num,cpa_conversion_rate,blocking_level,currency)VALUES(%(date)s,%(site)s,%(site_name)s,%(campaign)s,%(clicks)s,%(impressions)s,%(spent)s,%(ctr)s,%(cpm)s,%(cpc)s,%(cpa)s,%(cpa_actions_num)s,%(cpa_conversion_rate)s,%(blocking_level)s,%(currency)s)""",list1)
"""for i in list:
   for key.value in i.iteritems():
   print (key)"""

mydb.commit()
cursor.close()
print "Done"