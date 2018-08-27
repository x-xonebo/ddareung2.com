from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('123.html')


@app.route('/next', methods=['POST'])
def action():
    # location = request.form['location']
    return render_template('testest.html')

@app.route('/map/', methods=['POST'])
def result():
    maping = request.form['maping']
    return render_template('jidopage.html', maping=maping)
    
@app.route('/abcd')
def qwe():
    return render_template('parkpark.html')
if __name__ == '__main__':
    app.run(debug=True)