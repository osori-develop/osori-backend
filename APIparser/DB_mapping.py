import psycopg2
import configparser


#set config
config = configparser.ConfigParser()    
config.read('../config.ini', encoding='utf-8')

host = config['DB_config']['ip']
pw = config['DB_config']['pw']




#식단
class cbhs2_db :

    # 날짜 (2000-00-00) 분류(B,L,D) 메뉴를 인자로 전달하면 DB에 삽입해주는 코드
    def insert_menu ( day, BLD, MENU) :
        try :
            db = psycopg2.connect(host=host , dbname='cbhs2',user='cbhs',password=pw ,port=5432)
            cur=db.cursor()

            cur.execute("INSERT INTO CBHS2_MENU(DAY,BLD,MENU) VALUES(%s,%s,%s )",(day,BLD,MENU))
            db.commit()
            
            db.close()
            print("ok")

            return 1

        except Exception as e :
            print("에러 : " + str(e))
            return e

    # 해당 날짜와 분류의 메뉴 삭제
    def delete_menu (day,BLD) :
        
        try :
            db = psycopg2.connect(host=host , dbname='cbhs2',user='cbhs',password=pw ,port=5432)
            cur=db.cursor()

            cur.execute("DELETE FROM CBHS2_MENU WHERE DAY = %s and BLD = %s",(day,BLD))
            db.commit()
            
            db.close()

            print("ok")
            return 1

            
        except Exception as e :
            print("에러 : " + str(e))
            return e




    # DB에 저장되어있는거 모두 출력
    def all_menu_print() :
        try :
            db = psycopg2.connect(host=host , dbname='cbhs2',user='cbhs',password=pw ,port=5432)
            cur=db.cursor()

            cur.execute("SELECT * FROM CBHS2_MENU")
            re = cur.fetchall()
            for st in re :
                print(st)
            
            db.close()
            print("ok")

            return 1

        except Exception as e :
            print("에러 : " + str(e))
            return e




# 사용법
if __name__ == "__main__" :
    cbhs2 = cbhs2_db

    #cbhs2.insert_menu("2022-03-03", "B", "test")
    
    cbhs2.all_menu_print()
    #cbhs2.delete_menu("2022-03-03","B")





#공지사항

