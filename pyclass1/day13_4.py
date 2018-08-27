from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    dic = {'user':'hong1001','addr':'서울 도봉구', 'phone':'010-4563-9090'}
    return render_template('for_dict.html', dic=dic)


if __name__ == '__main__':
    app.run(debug=True)