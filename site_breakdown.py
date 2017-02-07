from __future__ import division


import requests


url = "https://backstage.taboola.com/backstage/api/1.0/cpxinteractive-sc/reports/campaign-summary/dimensions/site_breakdown?start_date=2017-1-17&end_date=2017-1-17"

headers = {'Authorization':'Bearer Ca4BAAAAAAAAEbkyAQAAAAAAGAEgACn0rhOyWQEAADooOWY3MTEzOTZlMDQwMDg5NzgxZWY3NWRkZmE3M2QxM2M4NWVkZDRiNEAC::f065c1::3fe113'}

r = requests.get(url,headers=headers)

print r.content