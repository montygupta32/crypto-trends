import json
from requests import Request, Session
from datetime import datetime

currency = 'INR'

global_url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?convert=' + currency

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'aeba1811-18bd-4699-89c7-f05d7b45cd64',
}
session = Session()
session.headers.update(headers)

request = session.get(global_url) # requesting the data
results = request.json() # formatting the data

#print(json.dumps(results, sort_keys = True, indent = 4))

#storing data in variables
active_currencies = results['data']['active_cryptocurrencies']
active_markets = results['data']['active_market_pairs']
bitcoin_percentage = results['data']['btc_dominance']
last_updated = results['data']['last_updated']
global_cap = results['data']['quote'][currency]['total_market_cap']
global_volume = results['data']['quote'][currency]['total_volume_24h']

#formatting the data
active_currencies_string = '{:,}'.format(active_currencies)
active_markets_string = '{:,}'.format(active_markets)
global_cap_string = '{:,}'.format(global_cap)
global_volume_string = '{:,}'.format(global_volume)
#last_updated_string = datetime.fromtimestamp(last_updated).strftime('%B %d, %Y at %I:%M%p')  #using conversion specifiers to make it readable

print()

print('There are currently ' + active_currencies_string + ' active cryptocurrencies and ' + active_markets_string + ' active markets.')
print('The global cap of all cryptos is ' + global_cap_string + ' and global volume is ' + global_volume_string + '.')
print('bitcoin\'s percentage of the global cap is ' + str(bitcoin_percentage) + '% .')
print()
print('The information was last updated on ' + str(last_updated) + ' .')
