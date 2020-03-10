#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 15:37
# @Author  : CaiChangEn
# @Email   : mail0426@163.com
# @Software: PyCharm
# 
#  Need nginx pass a header with access user ip X-Forwarded-For.
# 
from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def ip():
    remove_ip=request.host.split(':')[0]
    print(request.headers.get('X-Forwarded-For'))
    return remove_ip


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)