# [해커] Bithumb open API 활용하여,
# 실시간 BTC(Bitcoin) 현재가를 출력하는 crypto.py

import requests

# @app.route('/bitcoin')
# def bitcoin():
#     # 1. requests 통해 요청 보내기
#     currency = 500
#     url = ' https://api.bithumb.com/public/ticker/{currency}'
#     response = requests.get(url)
#     res_dict = response.json()

#     print(res_dict) 

# 1. requests 통해 요청 보내기
currency = 'BTC'
url = 'https://api.bithumb.com/public/ticker/'+currency
response = requests.get(url)
res_dict = response.json()

print(response)
print(res_dict['data']['opening_price']) 
