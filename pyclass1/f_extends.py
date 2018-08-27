from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index_extends.html')

@app.route('/about')
def about():
    return render_template('about_child.html')

if __name__ == '__main__':
    app.run(debug=True)

