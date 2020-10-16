#-*-coding:utf-8-*-
from user import etf_blue
import pymysql
from flask import Flask,render_template,request,url_for
#传入板块
style_list1 = [ '科技创新', '先进制造', '消费医药', '周期', '价值', '宽基']
# 传入宽基
wide_bench1 = [ '上证50', '中证100', '上证180', '沪深300', '中证500', '中证1000']
@etf_blue.route('/')
def index():
    conn = pymysql.connect(user='root', host='localhost', passwd='root', db='etf',cursorclass=pymysql.cursors.DictCursor, charset='utf8')
    cur = conn.cursor()
    dict_sector = {}
    dict_bench = {}
    for i in style_list1:
        S = i
        sql_filter = "select ETFname,ETFid from etf_cluster where sector='%s' order by ETFscale desc" % S
        cur.execute(sql_filter)
        data_filter = cur.fetchall()
        dict_sector[i] = data_filter
    for j in wide_bench1:
        S = j
        sql_filter1 = "select ETFname,ETFid from etf_cluster where target_name='%s' order by ETFscale desc" % S
        cur.execute(sql_filter1)
        data_filter1 = cur.fetchall()
        dict_bench[j] = data_filter1
    return render_template('home_page.html',dict_sector=dict_sector,dict_bench=dict_bench)