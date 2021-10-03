import requests
r = requests.get("https://in.tradingview.com/")
print(r.text)