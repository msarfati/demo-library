#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Demo-Library
# By Michael Sarfati (michael.sarfati@utoronto.ca), Feb 2015
from flask import Flask

app = Flask(__name__)
app.config.from_envvar('SETTINGS')
app.run(port=app.config['PORT'], debug=app.config['DEBUG'])
