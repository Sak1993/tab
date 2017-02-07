from __future__ import division

#!/usr/bin/python -tt


import requests

client_id = "3079549b0fc741ad9aded67054a99039"
client_secret = "fcc590a6867d4b28a8cbb81fc987fa77"
grant_type = "client_credentials"


payload = {
	'grant_type' : 'client_credentials',
	'client_id' : '3079549b0fc741ad9aded67054a99039',
	'client_secret' : 'fcc590a6867d4b28a8cbb81fc987fa77',

}

r = requests.post("https://backstage.taboola.com/backstage/oauth/token",
	data=payload)

print r.content