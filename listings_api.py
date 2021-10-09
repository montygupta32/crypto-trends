import json
from requests import Request, Session

listing_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'aeba1811-18bd-4699-89c7-f05d7b45cd64',
}

session = Session()
session.headers.update(headers)

request = session.get(listing_url) # requesting the data
results = request.json() # formatting the data

data = results['data']

#print(json.dumps(results, sort_keys = True, indent = 4))

for currency in data:
    rank = currency['cmc_rank']
    name = currency['name']
    symbol = currency['symbol']
    total_supply = currency['total_supply']
    price = currency['quote']['USD']['price']
    print(str(rank) + ': ' + name + '(' + symbol + ') ' + 'total supply = ' + str(total_supply) + ' price = ' + str(price))