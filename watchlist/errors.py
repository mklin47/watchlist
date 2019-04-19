#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:麦考林
@file: errors.py
@time: 2019/4/19 15:39
"""
from flask import render_template
from watchlist import app


# 错误处理函数
@app.errorhandler(404)  # 传入要处理的错误代码
def page_not_found(e):  # 接受异常对象作为参数
    return render_template('errors/404.html'), 404  # 返回模板和状态码


@app.errorhandler(400)
def page_not_found(e):
    return render_template('errors/400.html'), 400


@app.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500
