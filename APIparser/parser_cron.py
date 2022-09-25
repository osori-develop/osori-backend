
import requests
import datetime
import configparser
import DB_mapping
import parser.homepage_parser

#set config
config = configparser.ConfigParser()    
config.read('../config.ini', encoding='utf-8')

cbhs_app_Back_url = config['webhook']['cbhs_app_Back_url']


def webhook(text):
    url = cbhs_app_Back_url
    print(url)
    json = {'text' : text}
    requests.post(url, json = json)




def cron_cbhs2_menu () :
    re = parser.homepage_parser.get_cbhs2_menu()
    cbhs2 = DB_mapping.cbhs2_db
    
    for row in re :
        if len(row[2]) > 3 :
            cbhs2.insert_menu(row[0],row[1],row[2]);



    now = datetime.datetime.now()
    now = now.strftime("%m/%d/%Y, %H:%M:%S")
    
    str = now + "크론 실행 아래의 메뉴 디비에 추가" + cbhs2.all_menu_print()
    print(str)
    webhook(str)





if __name__ == "__main__" :

    cron_cbhs2_menu()