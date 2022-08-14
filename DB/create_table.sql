/*
메뉴 테이블 및 기타 유저 테이블 create sql

table 이름 규칙
주로 APIparser 에서 교체하는 것은 parser_tablename
주로 APImain 에서 교체하는 것은 main_tablename
아예 spase를 나눠도 되긴함...

DB 수정전 무조건 해당 파일 수정 후 커밋, 크러쉬 방지할 것
alter로 수정한것도 로그삼아 기록
*/

/* cbhs2_menu */
/*
메뉴 테이블 및 기타 유저 테이블 create sql

table 이름 규칙
주로 APIparser 에서 교체하는 것은 parser_tablename
주로 APImain 에서 교체하는 것은 main_tablename
아예 spase를 나눠도 되긴함...

DB 수정전 무조건 해당 파일 수정 후 커밋, 크러쉬 방지할 것
alter로 수정한것도 로그삼아 기록
*/

/* cbhs2_menu - 메뉴저장테이블

아이디
날짜
아ㅁㅋ

*/
CREATE TABLE CBHS2_MENU
(
	ID SERIAL PRIMARY KEY,
	DAY date NOT NULL,
    BLD VARCHAR(50) UNIQUE NOT NULL,
	MENU VARCHAR(355) UNIQUE NOT NULL,
	
    best integer  DEFAULT 0,
    worst integer  DEFAULT 0;
	
    
);