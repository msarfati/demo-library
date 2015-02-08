#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Demo-Library
# By Michael Sarfati (michael.sarfati@utoronto.ca), Feb 2015

from flask import Flask
from flask.ext.script import Manager, Shell, Server

app = Flask(__name__)
app.config.from_envvar('SETTINGS')

def _make_context():
    return dict(app=app)

manager = Manager(app)
manager.add_command("shell", Shell(make_context=_make_context))
manager.add_command("runserver", Server(port=app.config['PORT']))

if __name__ == '__main__':
    manager.run()
