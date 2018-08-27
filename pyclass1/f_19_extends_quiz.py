from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('showcase.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/designers')
def designers():
    return render_template('designers.html')

@app.route('/packages')
def packages():
    return render_template('packages.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)