from flask import Flask, render_template, request

# 객체 생성
app = Flask(__name__)

# 라우팅 - 연결 페이지
@app.route('/')
def home():
    return render_template('for_main.html')

@app.route('/gugu')
def gugu():
    return render_template('for_main2.html')

# 앱 실행
if __name__ == '__main__':
    app.run(debug=True)
