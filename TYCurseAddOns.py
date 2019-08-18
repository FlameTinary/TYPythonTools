#!/anaconda3/bin/ python
# -*- encoding: utf-8 -*-
'''
@File    :   TYCurseAddOns.py
@Time    :   2019/08/18 16:35:30
@Author  :   Sheldon 
@Version :   1.0
@Contact :   tinarychina@gmail.com
@License :   (C)Copyright 2018-2019, Sheldon
@Desc    :   None
'''

from urllib import request

baseUrl = "https://www.curseforge.com/wow/addons"
searchPath = "/search?category=&search="
headers = {"content-type": "text/html",'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

searchStr = 'AdvancedInterfaceOptions'

# print(baseUrl+searchPath+searchStr)

base_get = request.Request(baseUrl+searchPath+searchStr,headers=headers)
response = request.urlopen(base_get).read().decode('utf8')

print(response)