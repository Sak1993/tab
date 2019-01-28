import requests
import json
import pymysql
#url = "https://backstage.taboola.com/backstage/api/1.0/cpxinteractive-sc/reports/campaign-summary/dimensions/campaign_breakdown?start_date=2017-1-31&end_date=2017-1-31"

#headers = {'Authorization':'Bearer Ca4BAAAAAAAAEbkyAQAAAAAAGAEgACnI-237WQEAADooMDIyOGU2MWExYTJjNWQzOWIyYmViNmY5NDgyYjI1MTQxN2E4ZWU3YUAC::f065c1::3fe113'}

#r = requests.get(url,headers=headers)

#print r.content
#data = r.json()
#print "hiiiiiii"

#with open("/Users/sgottam/Documents/taboola/campaign_breakdown.json","w") as file4:
 #    json.dump(data,file4)


testFile = open("/Users/sgottam/Documents/taboola/campaign_breakdown.json")
data = json.load(testFile)

mydb = pymysql.connect(host='localhost',user='root',password='Sai',db='taboola',charset='utf8',port=3306)

cursor =mydb.cursor()

list1 = data["results"]

cursor.executemany("""INSERT INTO campaign_breakdown(campaign_name,campaign,clicks,impressions,spent,ctr,cpm,cpc,campaigns_num,cpa,cpa_actions_num,cpa_conversion_rate,currency)VALUES(%(campaign_name)s,%(campaign)s,%(clicks)s,%(impressions)s,%(spent)s,%(ctr)s,%(cpm)s,%(cpc)s,%(campaigns_num)s,%(cpa)s,%(cpa_actions_num)s,%(cpa_conversion_rate)s,%(currency)s)""",list1)
"""for i in list:
   for key.value in i.iteritems():
   print (key)"""

mydb.commit()
cursor.close()
print "Done"