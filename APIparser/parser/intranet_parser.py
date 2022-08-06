# hompage_parser.py
# 충북학사 인트라넷의 개인정보를 파싱하는 패키지 입니다.
import configparser
import os
from datetime import date, timedelta
from bs4 import BeautifulSoup
from pyrsistent import get_in
import requests

#메서드 설명 - 인풋값 - 아웃풋값


# 유저 정보 파싱 (id, name,floor,room,room_num, date)
def get_user_info(user) :
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
    res4 = session.get(mypage_url, data = mypage_xml)
    
    # xml 파싱
    xml_str = res4.text
    #print(xml_str)

    n=xml_str.find('<Col id="SCHAFS_NO">')
    if n == -1 :
        return -1;
    else :
        n += len('<Col id="SCHAFS_NO">')

    id = xml_str[n:n+7]

    n=xml_str.find('<Col id="RESCHR_NM">')
    if n == -1 :
        return -1;
    else :
        n += len('<Col id="RESCHR_NM">')

    name = xml_str[n:n+3]



    n=xml_str.find('<Col id="ROOM_NO">')
    if n == -1 :
        return -1;
    else :
        n += len('<Col id="ROOM_NO">')

    room = xml_str[n:n+4]

    if room[-1] == "호" :
        room = int(room[0:len(room)-1])
        floor = int(str(room)[0])
    else :
        room = int(room[0:len(room)])
        floor = int(str(room)[0:1])


    n=xml_str.find('<Col id="FLOOR_NO">')
    if n == -1 :
        return -1;
    else :
        n += len('<Col id="FLOOR_NO">')

    room_num = int(xml_str[n:n+2])



    return (id, name,floor,room,room_num, date.today())


# 유저가 존재하는지 확인 (1 = 이름과 비밀번호 맞음, -1 = 틀림)
def get_user_exist(user,password) :
    session = requests.session()

    ################################################################################
    login_url = 'http://1.246.219.13:8080/cbhsLoginStd.do'

    login_xml = '<?xml version="1.0" encoding="UTF-8"?>\
    <Root xmlns="http://www.nexacroplatform.com/platform/dataset">\
        <Parameters />\
        <Dataset id="dsSearch">\
            <ColumnInfo>\
                <Column id="USER_ID" type="STRING" size="256" />\
                <Column id="PASSWORD" type="STRING" size="256" />\
                <Column id="BRHS_CODE" type="STRING" size="256" />\
            </ColumnInfo>\
            <Rows>\
                <Row>\
                    <Col id="USER_ID">'+user+'</Col>\
                    <Col id="PASSWORD">'+password+'</Col>\
                    <Col id="BRHS_CODE">DS</Col>\
                </Row>\
            </Rows>\
        </Dataset>\
    </Root>'
    ################################################################################

    ################################################################################
    res = session.post(login_url, data = login_xml )

    # 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
    #res.raise_for_status() 

    #print(res)
    #print(res.text)
    xml_str = res.text
    if xml_str.find('<Col id="CNT">0</Col>') != -1:
        return -1
    elif xml_str.find('<Col id="CNT">1</Col>')  != -1 :
        return 1
    else :
        return -1


# 유저가 방에 있는지 확인 (1 = 있음, 0 = 없음, -1 = 유저없음)
def get_in_room(user) :

    session = requests.session()
    url = "http://1.246.219.13:8080/webinoutStatus.do"
    xml = '<?xml version="1.0" encoding="UTF-8"?>\
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">\
	<Parameters />\
	<Dataset id="dsInout">\
		<ColumnInfo>\
			<Column id="SCHAFS_NO" type="STRING" size="256" />\
			<Column id="BRHS_CODE" type="STRING" size="256" />\
		</ColumnInfo>\
		<Rows>\
			<Row>\
				<Col id="SCHAFS_NO">'+user+'</Col>\
				<Col id="BRHS_CODE">DS</Col>\
			</Row>\
		</Rows>\
	</Dataset>\
</Root>\
'  
    xml.encode('utf-8')
    res = session.post(url, data = xml)

    # 응답코드가 200 즉, OK가 아닌 경우 에러를 발생시키는 메서드입니다.
    #res.raise_for_status() 

    # print(res)
    # print(res.text)

    if res.text.find("입실") != -1 :
        return 1
    elif res.text.find("퇴실") != -1 :
        return 0
    else  :
        return -1


#유저의 상벌점 점수 (int )
def get_user_point(user) :
    session = requests.session()
    url = "http://1.246.219.13:8080/webRwrPnsSearch.do"

    xml ='<?xml version="1.0" encoding="UTF-8"?>\
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
</Root>\
    '

    res = session.post(url, data=xml)
    print(res.text)


#유저의 상벌점 목록 반환


# 유저 수리 등록 (number 01~07)
def post_fix_info(user, number ,str) :
    session = requests.session()
    url = "http://1.246.219.13:8080/webEstaRepaReqSave.do"

    xml = '<?xml version="1.0" encoding="UTF-8"?>\
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">\
	<Parameters />\
	<Dataset id="dsList">\
		<ColumnInfo>\
			<Column id="CHK" type="STRING" size="256" />\
			<Column id="IDX" type="STRING" size="256" />\
			<Column id="STDNT_SN" type="STRING" size="256" />\
			<Column id="FLOOR_NO" type="STRING" size="256" />\
			<Column id="ROOM_NO" type="STRING" size="256" />\
			<Column id="PROCESS_CD" type="STRING" size="256" />\
			<Column id="REQUST_CN" type="STRING" size="256" />\
			<Column id="PROCESS_DTLS" type="STRING" size="256" />\
			<Column id="REQUST_DT" type="STRING" size="256" />\
			<Column id="COMPT_DT" type="STRING" size="256" />\
			<Column id="COMPT_NO" type="STRING" size="256" />\
			<Column id="REQUST_SE_CD" type="STRING" size="256" />\
			<Column id="RESCHR_NM" type="STRING" size="256" />\
			<Column id="SCHAFS_NO" type="STRING" size="256" />\
			<Column id="ROOM_NO_HO" type="STRING" size="256" />\
			<Column id="LOGIN_ID" type="STRING" size="256" />\
			<Column id="BRHS_CODE" type="STRING" size="256" />\
		</ColumnInfo>\
		<Rows>\
			<Row type="insert">\
				<Col id="PROCESS_CD">' + number +  '</Col>\
				<Col id="REQUST_CN">' + str +'</Col>\
				<Col id="SCHAFS_NO">'+user+'</Col>\
				<Col id="LOGIN_ID">'+user+'</Col>\
				<Col id="BRHS_CODE">DS</Col>\
			</Row>\
		</Rows>\
	</Dataset>\
</Root>\
'

    res = session.post(url, data=xml.encode('utf-8'),headers={'Content-type': 'text/plain; charset=utf-8'})
    print(res.text)


# 유저 수 목ㅗ 반ㅏ

#외박신청
def post_user_stay_out(user, start_date, end_date, no) :
    
    session = requests.session()
    url = 'http://1.246.219.13:8080/overNightStDateChk.do'
    xml = '<?xml version="1.0" encoding="UTF-8"?>\
<Root xmlns="http://www.nexacroplatform.com/platform/dataset">\
	<Parameters />\
	<Dataset id="dsDetail">\
		<ColumnInfo>\
			<Column id="IDX" type="STRING" size="256" />\
			<Column id="RESCHR_NM" type="STRING" size="256" />\
			<Column id="SCHAFS_NO" type="STRING" size="256" />\
			<Column id="FLOOR_ROOM_NO" type="STRING" size="256" />\
			<Column id="STAYOUT_FR_DT" type="STRING" size="256" />\
			<Column id="STAYOUT_TO_DT" type="STRING" size="256" />\
			<Column id="STAYOUT_RESN" type="STRING" size="256" />\
			<Column id="STAYOUT_RESN2" type="STRING" size="256" />\
			<Column id="DSTN_NM" type="STRING" size="256" />\
			<Column id="DSTN_NM2" type="STRING" size="256" />\
			<Column id="BRHS_CODE" type="STRING" size="256" />\
			<Column id="PREV_FO_DT" type="STRING" size="256" />\
			<Column id="PREV_TO_DT" type="STRING" size="256" />\
			<Column id="ORGIN_SIGUN" type="STRING" size="256" />\
			<Column id="BB" type="STRING" size="256" />\
		</ColumnInfo>\
		<Rows>\
			<Row>\
				<Col id="IDX">7735</Col>\
				<Col id="RESCHR_NM">김영우</Col>\
				<Col id="SCHAFS_NO">20-2337</Col>\
				<Col id="FLOOR_ROOM_NO">4층&#32;407호</Col>\
				<Col id="STAYOUT_FR_DT">20220730</Col>\
				<Col id="STAYOUT_TO_DT">20220801</Col>\
				<Col id="BRHS_CODE">DS</Col>\
				<Col id="ORGIN_SIGUN">3</Col>\
				<Col id="BB">충주시</Col>\
			</Row>\
		</Rows>\
	</Dataset>\
</Root>\
    '
    res = session.post(url, data=xml.encode('utf-8'),headers={'Content-type': 'text/plain; charset=utf-8'})
    print(res.text)


if __name__ == '__main__':

    #print(get_user_exist('20-2337','1998d0207'))
    print(get_user_info('20-2337'))
    #print(get_in_room("20-2337"))

    #get_user_point("20-2337")

    str = "에어컨에서물이나옵니다."
    #post_fix_info("20-2337","07",str)
    
    post_user_stay_out('','','','')

    pass