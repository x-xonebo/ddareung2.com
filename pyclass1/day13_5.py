from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('quiz123123.html')

@app.route('/grade_result/', methods=['POST'])
def result():
    kor = request.form['kor']
    eng = request.form['eng']
    math = request.form['math']
    tot = int(kor) + int(eng) + int(math)
    avg = float(tot/3)
    return render_template('form_grade_result.html', kor=kor, eng=eng, \
    math=math, tot=tot, avg=avg)

if __name__ == '__main__':
    app.run(debug=True)