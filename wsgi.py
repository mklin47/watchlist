#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author:麦考林
@file: wsgi.py
@time: 2019/4/19 16:37
"""
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app
