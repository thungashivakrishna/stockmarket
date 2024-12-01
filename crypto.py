from coinbase.rest import RESTClient
from json import dumps

###Replace with your own API Keys

api_key = "dfghujik"
api_secret = "fghjkl"

client = RESTClient(api_key=api_key, api_secret=api_secret)

###Get account balances

accounts = client.get_accounts()
print(accounts)
