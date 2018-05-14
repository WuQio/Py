#!/usr/bin/python3
from flask import Flask, jsonify, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/todo/api', methods=['GET', 'POST'])
def api():
    json = request.args.get('args')
    print('\n\n' + json)
    return redirect(url_for('test', test=json))


@app.route('/<test>')
def test(test):
    return '<p>This is test ' + test + '...</p>'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        print(request.form.get('name'))
        print('****')
    return 'aaa'


@app.route('/a')
def a():
    return render_template('index.html')


@app.route('/ajax', methods=['GET', 'POST'])
def ajax():
    print(request.args.to_dict())
    return '/ajax return'


@app.route('/postform', methods=['GET'])
def postform():
    if request.method == 'POST':
        print(request.form.get('name'))


if "__main__" == __name__:
    app.run()
