import config 
import os
import json
import requests

from config import access_token, client_id, account_number

order_instructions = {
  "orderType": "MARKET",
  "session": "NORMAL",
  "duration": "DAY",
  "orderStrategyType": "SINGLE",
  "orderLegCollection": [
    {
      "instruction": "Sell",
      "quantity": 1,
      "instrument": {
        "symbol": "JE",
        "assetType": "EQUITY"
      }
    }
  ]
}

endpoint = f'https://api.tdameritrade.com/v1/accounts/{account_number}/orders'


headers = {"Authorization": f"Bearer {access_token}"}

content = requests.post(url = endpoint, headers=headers, json=order_instructions)
print(content)
print(content.content)

with open ('priceHistory.json','w') as file:
    data = content.json()
    json.dump(data,file)


#os.system(f'curl -X POST --header "Authorization: Bearer {access_token}" --header "Content-Type: application/json" -d "{order_instructions}" "https://api.tdameritrade.com/v1/accounts/454199960/orders" > response.txt')
