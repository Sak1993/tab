import json


with open('/Users/sgottam/git/taboola_api/db_config.json') as json_data_file:
    data = json.load(json_data_file)
print(data)
