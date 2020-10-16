#-*-coding:utf-8-*-
from flask import Flask
from user import etf_blue
app=Flask(__name__)
#3注册到蓝图app中
app.register_blueprint(etf_blue)
if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True,host="127.0.0.3")