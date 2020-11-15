import os
import json
import urllib.parse

dir = os.getcwd()
f = open(dir + r'\response.json',)
f2 = open(r'..\tdSecrets.json',)
response_dict = json.loads(f.read())
secrets_dict = json.loads(f2.read())

account_number = secrets_dict["account_number"]
account_password = secrets_dict["password"]
client_id = secrets_dict["client_id"]
refresh_token = response_dict['refresh_token']
refresh_token_encoded = urllib.parse.quote(refresh_token)

os.system(f'curl -X POST --header "Content-Type: application/x-www-form-urlencoded" -d "grant_type=refresh_token&refresh_token={refresh_token_encoded}&access_type=offline&code=&client_id=NKDKII8WRPZJI4BLV6JNDHF8HPUFMQ4L&redirect_uri=" "https://api.tdameritrade.com/v1/oauth2/token" > {dir}/stockbot/response.json')

access_token = response_dict['access_token']

f.close()
f2.close()
