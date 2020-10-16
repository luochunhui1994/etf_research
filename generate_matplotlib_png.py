import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
import pandas as pd
import datetime
import seaborn as sns
from user import etf_blue
#2装饰视图函数

def generate_matplotlib_png(datas):
    in_weight = pd.DataFrame(datas).groupby('industry')['stockweight'].sum()
    in_weight = in_weight.to_frame()
    in_weight['industry'] = in_weight.index
    labels = in_weight['industry']
    sizes = in_weight['stockweight']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=False, startangle=150)
    plt.axis('equal')
    plt.title("行业分布")
    time=datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
    png_name="my_matplotlib"+time+".png"
    plt.savefig(f"./static/{png_name}")
    plt.clf()
    return png_name