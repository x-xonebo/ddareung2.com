from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    foods = ['라면', '삼계탕', '떡국', '참치회']
    return render_template('for_list.html', foods=foods)

@app.route('/list1/')
def list1():
    list1 = [1,2,3,4,5,6,7]
    list2 = [8,3,4,6,7,5,3]
    return render_template('list123.html', list1=list1, list2=list2)



if __name__ == '__main__':
    app.run(debug=True)