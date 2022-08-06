import psycopg2
try :
    db = psycopg2.connect(host='cbhsosori.duckdns.org', dbname='cbhs2',user='cbhs',password='25xhdtls!@#',port=5432)

    cursor=db.cursor()
except :
    print("에러")


#식단

#공지사항

