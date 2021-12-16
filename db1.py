# db1.py
# 로컬 데이터베이스 엔진
import sqlite3

# 연결 객체 생성: 임시로 메모리에 저장 (Connection 클래스)
# con = sqlite3.connect(":memory:")
# con = sqlite3.connect("c:\\work\\test.db")
con = sqlite3.connect("c:\\work\\sample.db")

# 커서에서 실제 SQL구문을 실행 (Cursor 클래스)
cur = con.cursor()

# 테이블 구조 (테이블 스키마): SQL은 대소문자 구분 안함
cur.execute("create table Phonebook (Name text, PhoneNum text);")

# 1건 입력
cur.execute("insert into Phonebook values ('derick', '010-222');")
cur.execute("insert into Phonebook values ('messi', '010-333');")
cur.execute("insert into Phonebook values ('son', '010-444');")

name = "chaboom"
phoneNumber = "010-666"
cur.execute("insert into Phonebook values (?,?);", (name, phoneNumber))

datalist = (("tom", "010-234234"), ("dsp", "010-456"))
cur.executemany("insert into Phonebook values (?,?);", datalist)

# 검색
cur.execute("select * from Phonebook;")
# for row in cur:
#     print(row)

# print("---fetchone()---")
# print(cur.fetchone())
# print("---fetchmany(2)---")
# print(cur.fetchmany(2))

# print("---fetchall()---")
# cur.execute("select * from Phonebook;")
print(cur.fetchall())

con.commit()
    