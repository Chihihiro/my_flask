# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 14:21
# @Author  : Chihiro

from flask import Flask, render_template, request, redirect, session, url_for

# 实列化flask对象
app = Flask(__name__)
app.debug = True

USERS = {1: {'name': 'aaa', 'age': 18, 'text': '123fdasdasdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'},
         2: {'name': 'alxe', 'age': 12321, 'text': '2132131111111dssssssssssssssssssssvcvxcxcxcxcxcxcxcxcxc'}}


@app.route('/index', methods=['GET'])
def index():
    if request.method == 'GET':
        user = session.get('user_info')
        if not user:
            url = url_for('ll')
            return redirect(url)
        return render_template('index.html', user_dict=USERS)


@app.route('/login', methods=['GET', 'POST'], endpoint='ll')
def login():
    if request.method == "GET":
        return render_template('login.html')
    else:
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user_info'] = user
            # return redirect('https://www.cnblogs.com/wupeiqi/articles/7552008.html')
            return render_template('index.html')
        return render_template('login.html', error='密码错误')


@app.route('/detail/<int:nid>', methods=['GET'])
def detail(nid):
    info = USERS.get(nid)
    user = session.get('user_info')
    if not user:
        return redirect('/login')
    return render_template('detail.html', info=info)


if __name__ == '__main__':
    app.run()
