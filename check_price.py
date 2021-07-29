import requests
# Check ราคา Bitcoin Start
response = requests.get('https://api.bitkub.com/api/market/ticker')
data = response.json()

chk_btc = data['THB_BTC']['last']

print ('ราคา 1 Bitcoin ตอนนี้', f"{chk_btc:,}" , 'บาท')
# Check ราคา Bitcoin END