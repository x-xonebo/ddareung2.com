# 인클루드 기능이란?
# - 자주 사용되는 소스부분을 별도의 html로 생성
# - 필요한 부분에 삽입

# 관련 모듈 블러오기
from flask import Flask, render_template

# app 객체 생성
app = Flask(__name__)

# 라우터
# / -> index_main.html
@app.route('/')
def home():
    # html -> templates 폴더에 있어야함
    return render_template('index_main.html')

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)