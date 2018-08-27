import sqlite3
from flask import Flask, render_template, request

# 플라스크 생성
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('sqlite_table.html')
# 라우팅 - 연결페이지
@app.route('/employees')
def employees():
    # DB 연동
    conn = sqlite3.connect('test.db')
    # 실행자 생성
    cursor = conn.cursor()
    # sql 명령 실행 - employees 테이블의 모든 데이터를 조회해라
    cursor.execute(''' select LastName, FirstName, Title from employees;  ''')
    # 리스트로 저장하기
    result = cursor.fetchall()
    # print(result)
    return render_template('sqlite_index.html', result=result)

@app.route('/list5')
def list5():
    # DB 연동
    conn = sqlite3.connect('test.db')
    # 실행자 생성
    cursor = conn.cursor()
    # sql 명령 실행 - employees 테이블의 모든 데이터를 조회해라
    cursor.execute(''' select * from genres limit 7 ''')
    # 리스트로 저장하기
    result = cursor.fetchall()
    # print(result)
    return render_template('list5.html', result=result)

@app.route('/albumns')
def albumns():
    # DB 연동
    conn = sqlite3.connect('test.db')
    # 실행자 생성
    cursor = conn.cursor()
    # sql 명령 실행 - employees 테이블의 모든 데이터를 조회해라
    cursor.execute(''' select * from albums limit 20 ''')
    # 리스트로 저장하기
    result = cursor.fetchall()
    # print(result)
    return render_template('albumns.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
# db 종료
conn.close()
