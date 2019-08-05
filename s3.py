# -*- coding: utf-8 -*-
# @Time    : 2019/8/5 14:41
# @Author  : Chihiro

from flask import Flask
#实列化flask对象
app = Flask(__name__)
app.config.from_object('setting.DevelopmentConfig')

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
