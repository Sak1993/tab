import json
import MySQLdb

testFile = open("/Users/sgottam/Documents/taboola/campaign_site_day_breakdown.json")
data = json.load(testFile)


mydb = MySQLdb.connect(host='localhost',
   user='root',
   passwd='',
   db='taboola',)



cursor = mydb.cursor()

list1 =  data["results"]
taboo = cursor.execute('SELECT * from campaign_summary_by_site')

#sql = "INSERT INTO site_breakdown_report(cpa_conversion_rate,site_name,cpm,ctr,cpa,cpc,cpa_actions_num,spent,site,blocking_level,currency,impressions,clicks) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#cursor.executemany("INSERT INTO `site_breakdown_report`(`cpa_conversion_rate`,`site_name`,`cpm`,`ctr`,`cpa`,`cpc`,`cpa_actions_num`,`spent`,`site`,`blocking_level`,`currency`,`impressions`,`clicks`) VALUES(%d,%s,%d,%d,%d,%d,%d,%d,%s,%s,%s,%d,%d)",list1)
#cursor.execute('INSERT INTO site_breakdown_report(cpa_conversion_rate,site_name,cpm,ctr,cpa,cpc,cpa_actions_num,spent,site,blocking_level,currency,impressions,clicks)VALUES(11,"asdfsdf",22,33,44,55,66,77,"asdfasdf","adsfsda","sdfgtg",12,13)')
#taboo = cursor.executemany("""INSERT INTO campaign_summary_by_site(date,site,site_name,campaign,clicks,impressions,spent,ctr,cpm,cpc,cpa,cpa_actions_num,cpa_conversion_rate,blocking_level,currency)VALUES(%(date)s,%(site)s,%(site_name)s,%(campaign)s,%(clicks)s,%(impressions)s,%(spent)s,%(ctr)s,%(cpm)s,%(cpc)s,%(cpa)s,%(cpa_actions_num)s,%(cpa_conversion_rate)s,%(blocking_level)s,%(currency)s)""",list1)
'''for i in list1:
    for key,value in i.iteritems():
        print key'''
mydb.commit()
cursor.close()
print "taboo"