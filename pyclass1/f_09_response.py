from flask import Flask, render_template, request

app = Flask(__name__)




@app.route('/')
def home():
    return render_template('f_09.html')


# 결과처리
# form action
# request.form[폼필드name 값] : 폼필드에서 입력한 값이 저장되어 있다.
@app.route('/result', methods=['POST'])
def action():
    # 리스트 생성
    result_list=[]
    name = request.form['name']
    emailaddress = request.form['emailaddress']
    phonenumber = request.form['phonenumber']
    message = request.form['message']
    print(name, emailaddress, phonenumber, message)
    # 리스트로 저장
    result_list.append(name)
    result_list.append(emailaddress)
    result_list.append(phonenumber)
    result_list.append(message)
    print(result_list)
    return render_template('f_09_result.html', name=name, emailaddress=emailaddress, phonenumber=phonenumber, message=message)
#    return '완료'


if __name__ == '__main__':
    app.run(debug=True)
