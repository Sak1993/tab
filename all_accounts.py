import requests
import json
import unicodecsv
import codecs
import pymysql
from datetime import datetime, timedelta


# This function retreievs the access token and passes it onto the the needed fucntions, thereby not visibly displaying the access key.
def access_token_retrieve():

    payload = {

    'grant_type' : 'client_credentials',
    'client_id' : '3079549b0fc741ad9aded67054a99039',
    'client_secret' : 'fcc590a6867d4b28a8cbb81fc987fa77',

    }

    url = "https://backstage.taboola.com/backstage/oauth/token"
    r = requests.post(url, data = payload)

    data = json.loads(r.content)
    return data['access_token']

# This fucntions retrieves all the advertisers for the account cpxi-network.
def accounts_list_retrieve():


    url1 = "https://backstage.taboola.com/backstage/api/1.0/cpxi-network/advertisers/"

    headers1 = {"Authorization": "Bearer "+access_token}

    r = requests.get(url1, headers=headers1)

    json_output1 = r.content

    json_data1 = json.loads(json_output1)

    advertisers_list = json_data1["results"]

    accounts_list=[]

    for i in advertisers_list:
        accounts_list.append(i["account_id"])

    return accounts_list

# This function generates the report in the form of a JSON object and loads the necessary information into the database.
def report_retrieve_db_load():


    host = "https://backstage.taboola.com/backstage/api/1.0/"
    extra = "/reports/campaign-summary/dimensions"

    headers = {"Authorization": "Bearer "+access_token}

    dimensions = "campaign_site_day_breakdown"
    #start_date="2017-01-23T00:00Z"
    #end_date="2017-01-29T23:59Z"

    report_date_obj = datetime.utcnow()-timedelta(1)
    report_date = str(report_date_obj.date())
    start_date = report_date+"T00:00Z"
    end_date = report_date+"T23:59Z"

    testFile = open("/Users/sgottam/Documents/taboola/db_config.json")
    data = json.load(testFile)




    mydb = pymysql.connect(host=data["user"]["host"],
                        user=data["user"]["username"],
                        password=data["user"]["password"],
                        db=data["user"]["db"],
                        charset=data["user"]["charset"],port=int(data["user"]["port"]))
            
    cursor = mydb.cursor()
            
    for items in acc_list:
        site = host+items+extra
        url = site+"/"+dimensions+"?"+"start_date="+start_date+"&"+"end_date="+end_date

        r = requests.get(url,headers=headers)

        json_output = r.content

        json_data = json.loads(json_output)

        list1 = json_data["results"]
        

        cursor.execute('set global max_allowed_packet=67108864')
        cursor.executemany("""INSERT INTO campaign_site_day_breakdown(date,cpa_conversion_rate,site_name,ctr,campaign,cpa,cpc,cpa_actions_num,site,spent,blocking_level,currency,impressions,clicks,cpm)VALUES(%(date)s,%(cpa_conversion_rate)s,%(site_name)s,%(ctr)s,%(campaign)s,%(cpa)s,%(cpc)s,%(cpa_actions_num)s,%(site)s,%(spent)s,%(blocking_level)s,%(currency)s,%(impressions)s,%(clicks)s,%(cpm)s)""",list1)
        mydb.commit()

    #this selects the columns required for the report.  
    query = 'SELECT campaign_site_day_breakdown.date, campaign_site_day_breakdown.site, campaign_site_day_breakdown.site_name,campaign_day_breakdown.campaign_name,campaign_site_day_breakdown.campaign,campaign_site_day_breakdown.clicks,campaign_site_day_breakdown.impressions,campaign_site_day_breakdown.spent,campaign_site_day_breakdown.ctr,campaign_site_day_breakdown.cpm,campaign_site_day_breakdown.cpc,campaign_site_day_breakdown.cpa,campaign_site_day_breakdown.cpa_actions_num,campaign_site_day_breakdown.cpa_conversion_rate,campaign_site_day_breakdown.blocking_level,campaign_site_day_breakdown.currency FROM campaign_site_day_breakdown JOIN campaign_day_breakdown ON campaign_site_day_breakdown.campaign = campaign_day_breakdown.campaign'
    cursor.execute(query) 
    sq_data = cursor.fetchall()

    field_names = [i[0] for i in cursor.description]

    with codecs.open('results.csv','wb') as csvfile:
        writer = unicodecsv.writer(csvfile,encoding='utf-8')
        writer.writerow(field_names)
        writer.writerows(sq_data)
    cursor.close()

    print "completed the report laoding process!"


if __name__=="__main__":
    access_token = access_token_retrieve()
    acc_list = accounts_list_retrieve()
    print acc_list
    report_retrieve_db_load()
else:
    print "invalid access"




