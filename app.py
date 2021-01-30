#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: app.py
# Author: Kedar Kekan (4506537+kedarX@users.noreply.github.com)
# Description:
# A simple python application that exposes a route at '/' path and runs a http server on port 8080
###

import os

import flask
from flask import request, jsonify


app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, PICT!"

print("Welcome to docker demo!")
app.run(host='0.0.0.0', port=8080)
