# hompage_parser.py
# 충북학사 인트라넷의 개인정보를 파싱하는 패키지 입니다.
import configparser
import os

from bs4 import BeautifulSoup
import requests

#메서드 설명 - 인풋값 - 아웃풋값
def get_exist_user(user,password) :
    mypage_url = 'http://1.246.219.13:8080/webRwrPnsInfoSearch.do'
        
    mypage_xml = '<?xml version="1.0" encoding="UTF-8"?>\
    <Root xmlns="http://www.nexacroplatform.com/platform/dataset">\
        <Parameters />\
        <Dataset id="dsSearch">\
            <ColumnInfo>\
                <Column id="LOGIN_ID" type="STRING" size="256" />\
                <Column id="SEMSTR_SE_CD" type="STRING" size="256" />\
                <Column id="BRHS_CODE" type="STRING" size="256" />\
            </ColumnInfo>\
            <Rows>\
                <Row>\
                    <Col id="LOGIN_ID">'+user+'</Col>\
                    <Col id="SEMSTR_SE_CD">0</Col>\
                    <Col id="BRHS_CODE">DS</Col>\
                </Row>\
            </Rows>\
        </Dataset>\
    </Root>'    

    session = requests.session()
    res4 = session.get(mypage_url, data = mypage_xml )
    print(res4.text)



if __name__ == '__main__':
    get_exist_user('20-2337','19980207')
 