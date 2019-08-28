"""
python으로 telegram message 보내기
"""
import requests

token = '888992733:AAGTL_2G1FOfa5mYFb1cfXsHqKIp4e48H74'
base_url = 'https://api.telegram.org'
# (1) getUpdates()를 통해 chat_id를 가져옴
url = f'{base_url}/bot{token}/getUpdates'
response = requests.get(url)
res_dict = response.json()
chat_id = 'chat_id='+str(res_dict['result'][0]['message']['chat']['id'])

# (2) url을 조합하여 requests로 요청 보내기
#method = 'sendMessage?'
msg = '&text=집에 가자'

url = f'{base_url}/bot{token}/sendMessage?' + chat_id + msg

#requests.get(/sendMessage?chat_id=975161663&text=집가자')
requests.get(url)
#response = requests.get(url)
#print(response)