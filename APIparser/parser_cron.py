
import requests
import datetime
import configparser

#set config
config = configparser.ConfigParser()    
config.read('config.ini', encoding='utf-8')

cbhs_app_Back_url = config['webhook']['cbhs_app_Back_url']


def webhook(text):
    url = cbhs_app_Back_url
    print(url)
    json = {'text' : text}
    requests.post(url, json = json)





now = datetime.datetime.now()
now = now.strftime("%m/%d/%Y, %H:%M:%S")
print(now)

webhook(now)