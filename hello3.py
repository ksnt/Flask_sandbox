from flask import Flask
from flask import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return redirect('http://www.example.com')

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
