# 플라스크 모듈 불러오기
from flask import Flask

# app 객체 생성
app = Flask(__name__)

# 라우터데코레이터
# http://127.0.0.1:5000/ -> 무엇을 보여줄것인가?
@app.route("/")
# 뷰함수 -> 화면 표시 함수
def hello():
    return "<h1 style='text-align:center'> Hello World! </h1> \
    <p> \
    <a href='/test'>test 페이지로 이동</a> \
    <br><br>\
    <a href='/gallery'>gallery 페이지로 이동</a> \
    </p>"

@app.route('/test/')
def test():
    return "test page"

@app.route('/gallery/')
def gallery():
    return "<h1 style='text-align:center'> Hello World! </h1> \
    <img src='/static/1.jpg'>"

# 앱 실행
if __name__ == "__main__":
    app.run()