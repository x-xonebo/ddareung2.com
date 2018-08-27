# 플라스크 모듈 불러오기
from flask import Flask

# app 객체 생성
app = Flask(__name__)


@app.route("/")
# 뷰함수 -> 화면 표시 함수
def hello_world():
    return ""
# 동적 파라미터 전달하기
# 함수로 인자 전달
# http://127.0.0.1:5000/user/<값> 
# -> 뷰함수(인자) -> return 인자
@app.route('/users/<userId>')
def users(userId):
    return 'users is @s' % userId

@app.route('/user2/<userId>/<userName>')
def users2(userId, userName):
    return '아이디 %s, 이름 %s' %(userId, userName)

# 값 제한
# 기본 데이타 형이 string
# <데이터타입:변수명>
# 데이터타입 - <int:데이터변수명>, <float:데이터변수명>
@app.route('/news/<int:newsid>/<int:start>')
def news(newsid, start):
    return "뉴스 %s %s" %(newsid, start)

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)