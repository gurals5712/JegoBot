import os
import json
import random
import requests
from pytz import timezone
from datetime import datetime
from flask import Flask, request, jsonify

# 이모트
emote_list ='🌈', '😊', '☺️', '😄', '😃', '🤪', '🤩', '🤠', '🍗', '🍖', '🍔', '🍟', '🍕', '🥪', '🥙', '🌮', '🌯', '🥗', '🥘', '🥫', '🍝', '🍜', '🍲', '🍛', '🍣', '🍱', '🥟', '🍤', '🍙', '🍚', '🍘', '🍥', '🥠', '🍴', '🍽', '🥢'

# 플라스크
app = Flask(__name__)

# 초기버튼
@app.route('/keyboard')
def Keyboard():

    dataSend = {
        "type" : "buttons",
        "buttons" : ["🌈급식정보", "🌈도움말"]
    }

    return jsonify(dataSend)




@app.route('/message', methods=['POST'])
def Message():
    
    dataReceive = request.get_json()
    content = dataReceive['content']

    if content == u"🌈급식정보":


        dataSend = {
            "message": {
                "text": "시간대를 선택하세요"
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "내일의급식", "메인으로"]
    }
        }
    
    elif content == u"메인으로":

        dataSend = {
            "message": {
                "text": "아래에서 메뉴를 선택하세요"
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["🌈급식정보", "🌈도움말"]
    }
        }
        
        
    elif content == u"오늘의급식":

        with open('today.json') as today_data:  
            today_meal_menu = json.load(today_data)

        # 급식 데이터 가공
        meal_one = today_meal_menu['menu']['breakfast']
        meal_two = today_meal_menu['menu']['lunch']
        meal_three = today_meal_menu['menu']['dinner']
        today = today_meal_menu['menu']['date']

        today_info = "🌈" + today + "일 오늘의 급식 정보입니다\n\n"


        # 급식 데이터가 없을경우
        if not meal_one:
            list_one = "🤔아침이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_one = emote + '아침\n\n'
            for one in meal_one:
                list_one = list_one + '| ' + one + '\n'


        if not meal_two:
            list_two = "🤔점심이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_two = emote + '점심\n\n' 
            for two in meal_two:
                list_two = list_two + '| ' + two + '\n'


        if not meal_three:
            list_thr = "🤔저녁이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_thr = emote + '저녁\n\n' 
            for three in meal_three:
                list_thr = list_thr + '| ' + three + '\n'

        meal_data = today_info + list_one + '\n' + list_two + '\n' + list_thr



        dataSend = {
            "message": {
                "text": meal_data
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "내일의급식", "메인으로"]
    }
        }
    
                
    if content == u"내일의급식":
        
        with open('next.json') as nxday_data:  
            nxday_meal_menu = json.load(nxday_data)

        # 급식 데이터 가공
        meal_one = nxday_meal_menu['menu']['breakfast']
        meal_two = nxday_meal_menu['menu']['lunch']
        meal_three = nxday_meal_menu['menu']['dinner']
        nxday = nxday_meal_menu['menu']['date']

        today_info = "🌈" + nxday + "일 내일의 급식 정보입니다\n\n"
        

        # 급식 데이터가 없을경우
        if not meal_one:
            list_one = "🤔아침이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_one = emote + '아침\n\n'
            for one in meal_one:
                list_one = list_one + '| ' + one + '\n'


        if not meal_two:
            list_two = "🤔점심이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_two = emote + '점심\n\n' 
            for two in meal_two:
                list_two = list_two + '| ' + two + '\n'


        if not meal_three:
            list_thr = "🤔저녁이 존재하지 않습니다.🤔\n"
        else:
            emote = random.choice(emote_list)
            list_thr = emote + '저녁\n\n' 
            for three in meal_three:
                list_thr = list_thr + '| ' + three + '\n'

        meal_data = today_info + list_one + '\n' + list_two + '\n' + list_thr



        dataSend = {
            "message": {
                "text": meal_data
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["오늘의급식", "내일의급식", "메인으로"]
    }
        }
    


    elif content == u"🌈도움말":

        infolist = "돈까스 맛없음", "플리또 짱", "짬타 각", "현재버전 - V3.0"
        info = random.choice(infolist)

        dataSend = {
            "message": {
                "text": info
            },
        "keyboard": {
            "type" : "buttons",
            "buttons" : ["🌈급식정보", "🌈도움말"]
    }
        }
        
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000)

