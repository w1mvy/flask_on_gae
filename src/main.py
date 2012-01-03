#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
sys.path.insert(0, './libs.zip')
from google.appengine.ext.webapp.util import run_wsgi_app
from flask import Flask, render_template
from flaskext.wtf import Form
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    run_wsgi_app(app)
