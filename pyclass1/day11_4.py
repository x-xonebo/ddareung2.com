# 특정 html 페이지 연결하기
# 연결되는 html 페이지는 template 폴더에 저장되어 있어야 한다.  
# 
# 플라스크 모듈 불러오기
from flask import Flask, render_template

# app 객체 생성
app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route("/")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def hello_world():
    return render_template('index.html')

@app.route("/user")
# 뷰함수 -> 화면 표시 함수
# templates 폴더 아래의 index.html 로 연결
def user():
    return render_template('user.html')

# 앱 실행
if __name__ == "__main__":
    app.run(debug=True)
