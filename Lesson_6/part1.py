coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

def dictionary(coin, code):
    return dict(zip(coin, code))
print(dictionary(coin, code))