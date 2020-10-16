#-*-coding:utf-8-*-
from user import etf_blue
import pymysql
import pandas as pd
from flask import Flask,render_template,request,url_for
@etf_blue.route('/etf_filter')
def etf_list():
    #传入风格特征
    style_list=['无','科技创新','先进制造','消费医药','周期','价值','宽基']
    #传入宽基
    wide_bench=['无','上证50','中证100','上证180','沪深300','中证500','中证1000']
    return render_template('etf_filter.html',style_list=style_list,wide_bench=wide_bench)