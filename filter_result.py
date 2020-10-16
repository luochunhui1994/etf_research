import datetime
import pymysql
from flask import request,render_template
from datetime import timedelta
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
import seaborn as sns
from user import etf_blue
#2装饰视图函数
from generate_matplotlib_png import  generate_matplotlib_png

@etf_blue.route('/filter_result',methods=['POST'])
def filter_result():
    #获取规模数据
    scale1=request.values.get('scale1')
    scale2= request.values.get('scale2')
    #获取风格数据
    style_select=request.values.get('style_select')
    #获取指数数据
    index_select=request.values.get('index_select')
    #下面进行判断填入为空的情况
    if scale1=='':
        scale1=-10000
    else:
        scale1=float(scale1)
    if scale2=='':
        scale2=100000
    else:
        scale2=float(scale2)

    scale_str="ETFscale >%s and ETFscale<%s"%(scale1,scale2)
    sql_filter = "select * from etf_cluster where " + scale_str
    #判断板块为空情况
    if style_select != '无':
        sql_filter+=" and sector='%s' "%(style_select)
    if index_select != '无':
        sql_filter+=" and target_name='%s' "%(index_select)
    sql_filter+=' order by ETFscale desc'
    #连接上数据库
    conn = pymysql.connect(user='root', host='localhost', passwd='root', db='etf',cursorclass=pymysql.cursors.DictCursor, charset='utf8')
    cur = conn.cursor()
    cur.execute(sql_filter)
    data_filter = cur.fetchall()
    if data_filter==():
        data_filter='没有满足筛选条件的结果'
    else:
        data_filter = pd.DataFrame(data_filter)
    return  render_template('filter_result.html',data_filter=data_filter)
