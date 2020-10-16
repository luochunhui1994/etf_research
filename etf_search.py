#-*-coding:utf-8-*-
from flask import Flask,render_template,request,url_for
import os
import glob
import pymysql
import pandas as pd
import datetime
from datetime import timedelta
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

import seaborn as sns
from user import etf_blue
#2装饰视图函数
from generate_matplotlib_png import  generate_matplotlib_png

@etf_blue.route('/gets/',methods=['POST'])
def etf_search():
    conn = pymysql.connect(user='root', host='localhost', passwd='root', db='etf',cursorclass=pymysql.cursors.DictCursor, charset='utf8')
    cur = conn.cursor()
    S = request.values.get('question')
    sql="select stockname,stockweight,industry from table2  where ETFid='%s' order by stockweight  DESC  limit 20" %S
    sql_name="select distinct ETFname from table2 where ETFid='%s'" %S
    cur.execute(sql)
    datas = cur.fetchall()
    cur.execute(sql_name)
    datas1 = cur.fetchall()
    name_search = datas1[0].get('ETFname') + S
    path = './static'
    for infile in glob.glob(os.path.join(path, '*.png')):
        os.remove(infile)
    matplotlib_png = generate_matplotlib_png(datas)
    return render_template('etf_search.html',items=datas,name_search=name_search,
                           matplotlib_png=matplotlib_png)
