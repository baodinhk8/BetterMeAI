from pyvi import ViTokenizer, ViPosTagger
import requests
import json
import random


def xuly(message):
    message = message.lower()

    message = str(ViTokenizer.tokenize(message))

    data = '{"text":"'+message+'"}'

    api_token = "https://rasabetterme.herokuapp.com/model/parse"

    r = requests.post(api_token, data=data.encode('utf-8'), headers={
                      'Content-type': 'text/plain; charset=utf-8'})

    r = r.json()

    f = open('answer.json')
    data = json.load(f)

    conf = r["intent"]['confidence']
    intent = r["intent"]['name']

    for i in (data):
        if i == intent:
            respond = str(random.choice(data[i]["text"]))
            break

    conf = round(float(conf)*100)

    if(conf > 75):
        return respond

    return "Xin lỗi mình chưa được học mấy cái này, bạn dạy mình đi"
