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
@etf_blue.route('/single_etf/<string:single_etf>')
def single_etf(single_etf):
    conn = pymysql.connect(user='root', host='localhost', passwd='root', db='etf',cursorclass=pymysql.cursors.DictCursor, charset='utf8')
    cur = conn.cursor()
    S=single_etf
    sql="select stockname,stockweight,industry from table2  where ETFid='%s' order by stockweight  DESC  limit 20" %S
    sql_name="select distinct ETFname from table2 where ETFid='%s'" %S
    #基金信息：对标指数名称及其代码,规模，年华收益，跟踪误差
    sql_info = "select distinct target_name,target_index,ETFscale,年化收益率,跟踪误差 from table2 where ETFid='%s'" % S
    cur.execute(sql)
    datas = cur.fetchall()
    cur.execute(sql_name)
    datas1 = cur.fetchall()
    name_search = datas1[0].get('ETFname') + "("+S+")"
    cur.execute(sql_info)
    etf_info = cur.fetchall()
    target_name = etf_info[0].get('target_name')
    target_index = etf_info[0].get('target_index')
    ETFscale = etf_info[0].get('ETFscale')
    annu_return = etf_info[0].get('年化收益率')
    target_error = etf_info[0].get('跟踪误差')
    top_15=pd.DataFrame(datas)['stockweight'].sum(0)
    path = './static'
    for infile in glob.glob(os.path.join(path, '*.png')):
        os.remove(infile)
    matplotlib_png = generate_matplotlib_png(datas)
    return render_template('single_etf.html',items=datas,name_search=name_search,
    target_name=target_name,target_index=target_index,ETFscale=ETFscale,
    annu_return=annu_return,target_error=target_error,matplotlib_png=matplotlib_png,
    top_15=top_15
                           )