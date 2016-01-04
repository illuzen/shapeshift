import requests
import json
import pandas as pd
import matplotlib.pyplot as plt

url_stem = 'http://coincap.io/'


def get_price_history(symbol):
  response = requests.get('%spage/%s' % (url_stem, symbol))
  #print response.text
  data = json.loads(response.text)['price']
  prices = [row[1] for row in data]
  dates = pd.to_datetime([row[0] for row in data], unit='ms')
  return pd.Series(data=prices, index=dates)

def get_coin_list():
  response = requests.get('%scoins' % url_stem)
  return json.loads(response.text)


def combine_price_series(series):
  combined = pd.concat(series, axis=1).interpolate()
  return combined


xmr_series = get_price_history('XMR')
#print xmr_series
#btc_series = get_price_history('BTC')
orb_series = get_price_history('ORB')
#print btc_series
combined = combine_price_series([xmr_series, orb_series])
print combined
plt.plot(combined)
plt.show()

#obfs3 94.102.63.124:53381 f6a472f63db3f939e32b359a292dd08151563dd6
