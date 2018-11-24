import os
import json
import random
import requests
from pytz import timezone
from datetime import datetime
from flask import Flask, request, jsonify

#이모트
emote_list ='🌈', '😊', '☺️', '😄', '😃', '🤪', '🤩', '🤠', '🍗', '🍖', '🍔', '🍟', '🍕', '🥪', '🥙', '🌮', '🌯', '🥗', '🥘', '🥫', '🍝', '🍜', '🍲', '🍛', '🍣', '🍱', '🥟', '🍤', '🍙', '🍚', '🍘', '🍥', '🥠', '🍴', '🍽', '🥢'

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

        global d, strday, response, meal_menu
        d = datetime.now(timezone('Asia/Seoul'))
        strday = str(d.day)
        response = requests.get('https://schoolmenukr.ml/api/middle/M100000191?hideAllergy=true&date=' + strday)
        meal_menu = json.loads(response.text)
        
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
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "도움말"]
    }
        }
        

    elif content == u"아침":

        meal_one = meal_menu['menu']['breakfast']

        if not meal_one:
            list_one = "아침이 존재하지 않습니다.🤔"
        else:
            emote = random.choice(emote_list)
            list_one = emote + '아침\n\n'
            for one in meal_one:
                list_one = list_one + '| ' + one + '\n'

        dataSend = {
            "message": {
                "text": list_one
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
        

    elif content == u"점심":

        meal_two = meal_menu['menu']['lunch']
        
        if not meal_two:
            list_two = "점심이 존재하지 않습니다.🤔"
        else:
            emote = random.choice(emote_list)
            list_two = emote + '점심\n\n' 
            for two in meal_two:
                list_two = list_two + '| ' + two + '\n'
            
        dataSend = {
            "message": {
                "text": list_two
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["아침", "점심", "저녁", "메인으로"]
    }
        }
        
        
    elif content == u"저녁":

        meal_three = meal_menu['menu']['dinner']

        if not meal_three:
            list_thr = "저녁이 존재하지 않습니다.🤔"
        else:
            emote = random.choice(emote_list)
            list_thr = emote + '저녁\n\n' 
            for three in meal_three:
                list_thr = list_thr + '| ' + three + '\n'
            
        dataSend = {
            "message": {
                "text": list_thr
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
    app.run(host='0.0.0.0', port = 8000)

