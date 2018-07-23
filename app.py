from flask import Flask, render_template
from flask import request, json
import json
import jsonify



app = Flask(__name__)

@app.route('/')
def index():
    Aziiz = User('Aziiz', 'Ziana', 'aziizziana@gmail.com', 'devziana')
    return jsonAziiz = json.dumps(Aziiz, default=jsonDefault)

@app.route('/signup')
def signUp():
    return render_template('signup.html')

@app.route('/reportproblem')
def reportProblem():
    return render_template('report_problem.html')

@app.route('/approve')
def approve():
    data = {}
    data['key'] = 'value'
    json_data = json.dumps(data)
    print(2)
    return render_template('approve.html')

@app.route('/users')
def users():
    return 2

if __name__ == '__main__':
      app.run()
