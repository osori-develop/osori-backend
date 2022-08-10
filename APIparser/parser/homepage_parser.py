import configparser
from datetime import datetime
#from django.utils.dateformat import DateFormat

from bs4 import BeautifulSoup
import requests

# requests
menu_url = requests.get('http://www.cbhs2.kr/meal?searchWeek=0')
html = menu_url.text
soup = BeautifulSoup(html, 'lxml')


find_class = soup.find('div', class_ = 'fplan_plan')
print_day = find_class.find('a', class_ = 'btn_type1 fplan_date_sun')
print_rice = find_class.find('h3')
print_menu = find_class.find('p')


week_menu = [{}, {}, {}, {}, {}, {}, {}]

i = 0
#for ele in soup.find_all('div', class_ = 'fplan_plan'):
for ele in soup.find_all(attrs={'class': 'fplan_plan'}):
        
    text = ele.text
    
    date = text.split('\n')
    DATE = date[2].split('(')[0]  # date
    DATE = DATE.strip()
    if (  not(date[7] == '\t\t\t\t\t\xa0') ):
        
        a = 7
        B = ''
        while True:
            if (date[a] == '중식'):
                a = a + 1
                break
            B += date[a].strip()
            B += ' '
            a = a + 1
        
        #7번 이후로 리스트가 깨지니까 여기선 for문을 이용해서 \t\t\t나오기 전까지 메뉴 저장으로 해야하나?
        b = a
        L = ''
        while True:
            if (date[b] == '석식'):
                b = b + 1
                break
            
            L += date[b].strip()
            L += ' '
            b = b + 1
        
        c = b
        D = ''
        while True:
            if (date [c] == '\t\t\t'):
                break
            
            D += date[c].strip()
            D += ' '
            c = c + 1
        

        B = B.replace(', ', ' ')
        L = L.replace(",", " ")
        D = D.replace(",", " ")

        B = B.replace('\t', '')
        L = L.replace('\t', '')
        D = D.replace('\t', '')


    else:
        B = "메뉴가 없어요."
        L = "메뉴가 없어요."
        D = "메뉴가 없어요."
        
    

    print(DATE)
    print(B)
    print(L)
    print(D)
    print()
    
    
    

    
        