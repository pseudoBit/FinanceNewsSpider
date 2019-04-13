#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
from urllib2 import urlopen
import re

news_arr = []

bot_api = '' # bot api
user_api = [''] # channel link : @...

# This program works only for python 2.7

# if has Chinese, apply decode()

import threading

def printit():

    global last_news

    threading.Timer(15.0, printit).start()

    html = urlopen("http://119.29.63.230/24h/news_fbe.json?newsid=0").read().decode('utf-8')

    var_exists = 'last_news' in locals() or 'last_news' in globals()
    if var_exists:
        update_index =  int(str(re.findall(r'"newsID":"(.+?)",',html)[0])) - last_news
    else:
        update_index = 21

    if update_index > 0:
        rev_list = range(min(update_index+5,20))
        news_id = re.findall(r'"newsID":"(.+?)",',html)
        news_time = re.split(r'\s',str(re.findall(r'"time":"(.+?)",',html)))
        news_moment = news_time[1::2]
        news_day = news_time[0::2]
        news_day[0] = news_day[0][1:]
        news_content = re.findall(r'"content":"(.+?)",',html)
        for ix in rev_list[::-1]:
            if str(news_id[ix]) not in news_arr:
                news_arr.append(str(news_id[ix]))
                news_temp = news_day[ix][7:12].encode('utf-8') + str(' ') + news_moment[ix][0:5].encode('utf-8')  + str(' ') + news_content[ix].encode('utf-8')
                for user_num in range(len(user_api)):
                    urlopen("https://api.telegram.org/bot"+bot_api+"/sendMessage?chat_id="+user_api[user_num]+"&text="+news_temp).close()
        last_news = int(str(news_id[0]))
    if len(news_arr)>50:
        del news_arr[0:20]

printit()
