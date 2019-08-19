#!/anaconda3/bin/python
# -*- encoding: utf-8 -*-
'''
@File    :   TYChartRobot.py
@Time    :   2019/08/09 16:35:30
@Author  :   Sheldon 
@Version :   1.0
@Contact :   tinarychina@gmail.com
@License :   (C)Copyright 2018-2019, Sheldon
@Desc    :   None
'''

# here put the import lib

import json
import urllib.request

apiKey = "75bb96f437d141d4aaae63707ef62cc3"
userID = "OnlyUseAlphabet"
api_url = "http://openapi.tuling123.com/openapi/api/v2"

# text_input = input('我:')
text_input = "天气"

req = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": text_input
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "来广营"
            }
        }
    },
    "userInfo": {
        "apiKey": apiKey,
        "userId": userID
    }
}

req = json.dumps(req).encode('utf8')

# print(req)

headers = {'content-type': 'applocation/json'}
http_post = urllib.request.Request(api_url, data=req, headers=headers)
response = urllib.request.urlopen(http_post)
response_str = response.read().decode('utf8')
# print(response_str)
response_dic = json.loads(response_str)

response_code = response_dic['intent']['code']
response_text = response_dic['results'][0]['values']['text']
print('小薇:')
print('code:' + str(response_code) + ',' + 'text:' + response_text)