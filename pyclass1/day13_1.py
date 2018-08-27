from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('if_else_main.html')


@app.route('/score/<int:score>')
def score(score):
    return render_template('if_else_result.html', score=score)


# 0 < score2 < 20 -> 20보다 작습니다.
# score2 >= 20 -> 20보다 크거나 같습니다.
@app.route('/score2/<int:score2>')
def score2(score2):
    return render_template('if_else_result2.html', score2=score2)

@app.route('/age/<int:age>')
def age(age):
    return render_template('if_else_age.html', age=age)


if __name__ == '__main__':
    app.run(debug=True)
