#-*-coding:utf-8-*-
from flask import Blueprint
#1创建蓝图对象
etf_blue=Blueprint('etf',__name__)
from user import  home_page
from user import  etf_search
from user import etf_filter
from user import filter_result
from user import single_etf