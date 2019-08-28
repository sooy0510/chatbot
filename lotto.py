"""
requests를 통해 동행복권 API요청을 보내어,
1등 번호를 가져와 python list로 만듬
"""
import requests

# 1. requests 통해 요청 보내기
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'
response = requests.get(url)
res_dict = response.json()
# 이제 dict처럼 다룰 수 있는 상태

print(res_dict) 
#print(res_dict['drwtNo1']) 

# 1등 번호 6개가 담긴 result라는 list를 출력
result = []
for i in range(1,7):
    idx = 'drwtNo'+str(i)
    result.append(res_dict[idx])
print(result)