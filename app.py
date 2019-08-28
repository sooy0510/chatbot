from flask import Flask
import random
app = Flask(__name__)
@app.route('/')
def home():
    return 'hello'

# 1. 주문서를 만들고 -> @app.route('/name') 부분
# / : root
# 2. 해당 주문이 들어왔을 때 무엇을 할지 정의

@app.route('/name')
def name():
    return '오은애'

# Variable routing : <>
# 사용자가 입력한 값을 name 변수에 대입
@app.route('/hello/<name>')
def hello(name):
    return f'hello {name}'

@app.route('/square/<int:num>')
def square(num):
    # number를 제곱하여 반환
    return f'{str(num ** 2)}'

@app.route('/menu')
def menu():
    foods = ['대우식당','고갯마루','진가와','바스버거']

    res = random.choice(foods)
    return f'{res}'

@app.route('/lotto')
def lotto():
    # .sort : 원본까지 정렬
    # sorted() : 복사본만 정렬
    winner = [3,5,12,13,33,39]
    user = sorted(random.sample(range(1,46),6))

    # 만약 6개의 숫자가 모두 일치하면 1등
    # 만약 5개의 숫자가 일치하면 3등
    # 만약 4개의 숫자가 일치하면 4등
    # 만약 3개의 숫자가 일치하면 5등

    # set : 집합 자료구조
    # & : 교집합
    cnt = set(winner) & set(result)
    for i in winner:
        if i in user :
            cnt += 1
    res = '꽝'
    if cnt == 6 :
        res ='1등'
    elif cnt == 5 :
        res = '3등'
    elif cnt == 4 :
        res = '4등'
    elif cnt == 3:
        res = '5등'
    return f'{user,res}'