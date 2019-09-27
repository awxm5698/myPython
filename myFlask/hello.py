#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


tasks = [
        {
            'id': 1,
            'title': u'OSPA',
            'description': u'This is ospaf-api test',
            'done': False
        },
        {
            'id': 2,
            'title': u'Garvin',
            'description': u'I am garvin',
            'done': False
        }]


@app.route('/login', methods=['GET'])
def login():
    return render_template('login.html', name='wo shi shu?')


@app.route('/list', methods=['GET'])
def my_list():
    return render_template('list.html', navigation=[{'href': 1, 'caption': 1}, {'href': 2, 'caption': 2}])


@app.route('/base', methods=['GET'])
def base():
    return render_template('base.html', head='HHHHHH',content='WWWWWWWW')


@app.route('/json', methods=['GET'])
def response_json():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run()
