import sqlite3
from flask import Flask, render_template, request

# DB
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

def newTable():
    # 테이블 생성하기
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute(''' create table if not exists persons
        (username text, userage int, usergender text, usermajor text );
    ''')
    # DB에 반영
    conn.commit()
    # 조회 
    cursor.execute('select * from persons ')
    result_list = cursor.fetchall()
    print(result_list)
    # DB 닫기
    conn.close()



def insertData(username, userage, usergender, usermajor):
# 테이블에 데이터 삽입하기
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = 'insert into persons values (?,?,?,?)'
    cursor.execute(sql, (username,userage,usergender,usermajor))
    conn.commit()

# insertData('김준수',21,'남','기계공학과')

# 조회
def showTable_list():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('select * from persons; ')
    result_list = cursor.fetchall()
    print(result_list)
    return result_list

# 플라스크 생성
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('sqlite2_index.html')

# 라우팅 - 연결페이지 - 테이블 조회 페이지
@app.route('/showtable')
def showtable():
    result_list = showTable_list()
    return render_template('showtable.html', result_list = result_list)
# 데이터 입력 페이지
@app.route('/insertdata')
def insertdata_form():
    return render_template('insertdata_form.html')

# 데이터 입력처리 페이지
@app.route('/action', methods=['POST'])
def action():
    username = request.form['username']
    userage = request.form['userage']
    usergender = request.form['usergender']
    usermajor = request.form['usermajor']
    insertData(username, userage, usergender, usermajor)
    return render_template('action.html')


# 플라스크 실행
if __name__ == '__main__':
    app.run(debug=True)
# db 종료
conn.close()
