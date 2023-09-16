# app.py
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

# @app.route('/test')
# def hello_world():
    # return render_template('test.html')

if __name__ == '__main__':
    app.run(debug=True) 