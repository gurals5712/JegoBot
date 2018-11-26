import json
import time
import schedule
import requests
from pytz import timezone
from datetime import datetime


def parse():
    d = datetime.now(timezone('Asia/Seoul'))
    str_today = str(d.day)
    str_nxday = str(d.day + 1)
    td_response = requests.get('https://schoolmenukr.ml/api/middle/M100000191?hideAllergy=true&date=' + str_today)
    nx_response = requests.get('https://schoolmenukr.ml/api/middle/M100000191?hideAllergy=true&date=' + str_nxday)
    today_meal_menu = json.loads(td_response.text)
    nxday_meal_menu = json.loads(nx_response.text)
        
    with open('today.json', 'w', encoding="utf-8") as make_file:
        json.dump(today_meal_menu, make_file, ensure_ascii=False, indent="\t")

    with open('next.json', 'w', encoding="utf-8") as make_file:
        json.dump(nxday_meal_menu, make_file, ensure_ascii=False, indent="\t")

schedule.every().day.at("00:00").do(parse)

while True:
    schedule.run_pending() 
    time.sleep(1)