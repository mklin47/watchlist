#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:麦考林
@file: app.py
@time: 2019/4/18 16:17
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'
