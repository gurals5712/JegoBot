import os
import json
import random
import requests
from pytz import timezone
from datetime import datetime 
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

#급식파싱 API

d = datetime.now(timezone('Asia/Seoul'))
strday = str(d.day)
response = requests.get('https://schoolmenukr.ml/api/middle/M100000191?hideAllergy=true&date=' + strday)
meal_menu = json.loads(response.text)

#테스트 코드
#print(meal_menu['menu']['lunch'])


app = Flask(__name__)

#초기버튼
@app.route('/keyboard')
def Keyboard():

    dataSend = {
        "type" : "buttons",
        "buttons" : ["오늘의급식", "도움말"]
    }

    return jsonify(dataSend)




@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    
    if content == u"오늘의급식":
        dataSend = {
            "message": {
                "text": "시간대를 선택하세요"
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
    
                
    elif content == u"메인으로":
        dataSend = {
            "message": {
                "text": "아래에서 메뉴를 선택하세요"
            },''
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "도움말"]
    }
        }
        

    elif content == u"아침":
        meal_one = str(meal_menu['menu']['breakfast'])
        if meal_one == '[]' :
            meal_one = "데이터 값이 없습니다."
            
        dataSend = {
            "message": {
                "text": meal_one
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
        

    elif content == u"점심":
        meal_two = str(meal_menu['menu']['lunch'])
        if meal_two == '[]' :
            meal_two = "데이터 값이 없습니다."
        dataSend = {
            "message": {
                "text": meal_two
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
        
        
    elif content == u"저녁":
        meal_three = str(meal_menu['menu']['dinner'])
        if meal_three == '[]' :
            meal_three = "데이터 값이 없습니다."
        dataSend = {
            "message": {
                "text": meal_three
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
        

    elif content == u"도움말":
        infolist = "돈까스 맛없음", "플리또 짱", "짬타 각"
        info = random.choice(infolist)
        dataSend = {
            "message": {
                "text": info
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "도움말"]
    }
        }
        
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)

