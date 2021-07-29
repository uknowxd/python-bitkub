import requests

response = requests.get('https://api.bitkub.com/api/market/ticker')
data = response.json()

# เช็คแค่สกุลเงินเดี๋ยว
#chk_btc = data['THB_BTC']['last']
#print ('ราคา 1 Bitcoin ตอนนี้', f"{chk_btc:,}" , 'บาท')


# เช็คแบบหลายสกุลเงิน
name_coin = ['THB_BTC','THB_ETH','THB_DOGE']
while True:
    for n_coin in name_coin:
        m_coin = data[n_coin]
        last_price = m_coin['last']
        print(n_coin, f"{last_price:,}" , 'บาท')
    break